import discord
import modules.joinrelated as jn
import modules.userrelated as usr
import modules.guildrelated as gd
import modules.musicrelated as mu

commandList = {
    "!test" : usr.test,
    "!list" : gd.helpfunc,
    "!help" : gd.helpfunc,
    "!random" : usr.randomize,
    "!serverinfo" : gd.serverinfo,
    "!users" : gd.serverinfo,
    "!botinfo" : gd.botinfo,
    "!hello" : usr.hello,
    "!link" : gd.linkVoiceStream,
}

# Need a client argument passed
commandList2 = {
    "!thumb" : usr.thumb,
    "!wavecheck" : usr.wavecheck,
    "!gentest" : jn.test_welcome,
}

commandListMusic = {
    "!join" : mu.join,
    "!yt" : mu.yt,
    "!stream" : mu.stream,
    "!volume" : mu.volume,
    "!stop" : mu.stop,
}

async def detect_command(client, message):
    for comm, func in commandList.items():
        if comm in message.content:
            return await func(message)

    for comm, func in commandList2.items():
        if comm in message.content:
            return await func(client, message)

    for comm, func in commandListMusic.items():
        if comm in message.content:
            if isinstance(message.channel, discord.DMChannel):
                return await message.channel.send("Must be in a server voice channel")

            if message.author.voice is None:
                return await message.channel.send("Must be in a server voice channel")
            
            if client.voice_clients is None:
                return await message.channel.send("Must be in a server voice channel")

            return await func(client, message)
