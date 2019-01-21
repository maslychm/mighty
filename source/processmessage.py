from plugins.randomize import randomize
import random

async def detect_command(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await message.channel.send('Calculating messages...')
        async for msg in message.channel.history(limit=100):
            if msg.author == message.author:
                counter += 1
        await tmp.edit(content=f'You have {counter} messages.')

    if message.content.startswith('!hello'):
        await message.channel.send(f'Hello {message.author.mention}')

    if message.content.startswith('!info'):
        msg = 'Written by mighty_lord#4526'
        await message.channel.send(msg)

    if message.content.startswith('!help'):
        msg = 'avaliable commands:\n' + \
            '`!help` `!test` `!info` `!hello` `!random`'
        await message.channel.send(msg)

    if message.content.startswith('!hewwo :3'):
        msg = 'Ayy you found an eastern egg `nuzzles`'
        await message.channel.send(msg)

    if message.content.startswith("!random"):
        msg = randomize(message)
        await message.channel.send(msg)
        return
        
    if message.content.startswith('!roll'):
        await message.channel.send(f"`{random.randint(1,6)}`")
        return