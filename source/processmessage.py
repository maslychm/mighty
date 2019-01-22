# Check if message contains a command

from plugins.randomize import randomize
from plugins.logging import logging
from plugins.serverinfo import serverinfo
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

    if messagetext.startswith('!hello'):
        await channel.send(f'Hello {message.author.mention}')

    if messagetext.startswith('!info'):
        msg = 'Written by mighty_lord#4526 \n' + \
            'https://github.com/maslychm/mighty'
        await channel.send(msg)

    if messagetext.startswith('!help'):
        msg = 'avaliable commands:\n' + \
            '`!help` `!test` `!info` `!hello` `!random` `!users` `!serverinfo`'
        await channel.send(msg)

    if messagetext.startswith('!hewwo :3'):
        msg = 'Ayy you found an eastern egg `nuzzles`'
        await channel.send(msg)

    if messagetext.startswith("!random"):
        msg = randomize(message)
        await channel.send(msg)
        
    if messagetext.startswith('!roll'):
        await channel.send(f"`{random.randint(1,6)}`")

    if messagetext.startswith('!log'):
        logging(client)
        return
    
    if messagetext.startswith('!serverinfo') or messagetext.startswith('!users'):
        msg = serverinfo(client,message)
        await channel.send(msg)

    return