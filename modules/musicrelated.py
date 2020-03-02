import asyncio
import discord
import youtube_dl

'''
When I was reading more of documentation for how this all works,
I realized that my solution is horrible, but for the sake of not
spending 10 hours on making this perfect, I'll have some workarounds
and might come back to make this portion of code more salable
'''

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format' : 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}

ffmpeg_options = {
    'options' : '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')
    
    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

async def join(client, message):
    channel = message.author.voice.channel

    if len(client.voice_clients):
        return await client.voice_clients[0].move_to(channel)

    await channel.connect()

async def stop(client, ctx):
    if len(client.voice_clients):
        await client.voice_clients[0].disconnect()
    else:
        return

async def stream(client, message):
    """Streams from a url (same as yt, but doesn't predownload)"""

    await join(client, message)

    text = message.content.split()

    if len(text) != 2:
        return await message.channel.send("Use: `!stream YOURLINK`")
    
    url = text[1]
    
    try:
        async with message.channel.typing():
            player = await YTDLSource.from_url(url, stream=True)
            client.voice_clients[0].play(player, after=lambda e: print('Player error: %s' % e) if e else None)
    except (youtube_dl.utils.DownloadError, youtube_dl.utils.ExtractorError):
        return await message.channel.send("Something is wrong with the link")
    except discord.ClientException:
        await stop(client, None)
        await stream(client, message)
        return

    await message.channel.send('Now playing: {}'.format(player.title))

async def volume(client, message):
    """Changes the player's volume"""

    text = message.content.split()

    if len(text) != 2:
        return await message.channel.send("Use: `!volume PERCENT`")

    volume = int(text[1])

    client.voice_clients[0].source.volume = volume / 100
    await message.channel.send("Changed volume to {}%".format(volume))