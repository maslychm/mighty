# Check if message contains a command

from plugins import randomize
from plugins import serverinfo
from plugins import examples
from plugins import helps
from plugins import onjoin
import random

async def detect_command(client, message):
    messagetext = message.content
    channel = message.channel

    if messagetext.startswith('!test'):
        counter = 0
        tmp = await channel.send('Calculating messages...')
        async for msg in channel.history(limit=100):
            if msg.author == message.author:
                counter += 1
        await tmp.edit(content=f'You have {counter} messages.')
        return

    if messagetext.startswith('!hello'):
        await channel.send(f'Hello {message.author.mention}')
        return

    if messagetext.startswith('!info'):
        msg = 'Written by mighty_lord#4526 \n' + \
            'https://github.com/maslychm/mighty'
        await channel.send(msg)
        return

    if messagetext.startswith('!help') or messagetext.startswith('!list'):
        await helps.helps(client,message)
        return

    if messagetext.startswith('!hewwo :3'):
        msg = 'Ayy you found an eastern egg `nuzzles`'
        await channel.send(msg)
        return

    if messagetext.startswith("!random"):
        msg = randomize.randomize(message)
        await channel.send(msg)
        return
        
    if messagetext.startswith('!roll'):
        await channel.send(f"`{random.randint(1,6)}`")
        return

    if messagetext.startswith("!wavecheck"):
        msg = await examples.wavecheck(client,message)
        await channel.send(msg)
        return
    
    if messagetext.startswith('!serverinfo') or messagetext.startswith('!users'):
        msg = serverinfo.serverinfo(client,message)
        await channel.send(msg)
        return

    if messagetext.startswith('!thumb'):
        await examples.thumb(client,message)
        return

    if messagetext.startswith('!gentest'):
        await onjoin.test_welcome(client,message)
        return

    # Hardcoding my id to make sure it's me shutting down :)
    if 'shutdown' in messagetext and message.author.id == 232346727221297164:
        quit()