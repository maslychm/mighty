import discord
import random
import asyncio

async def test(message):
    counter = 0
    tmp = await message.channel.send('Calculating messages...')
    async for msg in message.channel.history(limit=100):
        if msg.author == message.author:
            counter += 1
    await tmp.edit(content=f"You've sent {counter} messages.")

async def thumb(client,message):
    channel = message.channel
    await message.channel.send('Send me that 👍 reaction, mate')

    def check(reaction, user):
        return user == message.author and str(reaction.emoji) == '👍'

    try:
        reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
    except asyncio.TimeoutError:
        await channel.send('👎')
    else:
        await channel.send('👍')

async def wavecheck(client,message):
    """
    !wavecheck @mention
    Wavecheck somebody in 3+ users channel
    Only the first user on the mention list will be checked
    """

    if isinstance(message.channel, discord.DMChannel):
        return "Sorry, no wavechecking in DMs"
    if not message.mentions:
        return "You have to mention a user to wavecheck them"
    
    # Get first mentioned member
    mentioned = message.mentions[0]

    await message.channel.send(f"{mentioned.mention}, you have 20 seconds to respond...")

    # Check if the mentioned user responded with key phrase
    def check(m):
        return (("test" in m.content.lower()
        or "my waves drippin" in m.content.lower()) 
        and m.channel == message.channel 
        and m.author == mentioned)

    try:
        await client.wait_for('message', timeout=20.0, check=check)
    except asyncio.TimeoutError:
        await message.channel.send(f"{mentioned.mention} got no waves")
    else:
        await message.channel.send(f"{mentioned.mention}'s waves DRIPPIN")

async def randomize(message):
    
    randomize_format = '''`Error:` Incorrect format
                use `!random a to b`
                where a and b are numbers and a < b
                '''

    def inner_parse(gen):
        if len(gen) == 1:
            return random.randint(1,100)
        if len(gen) < 4:
            return randomize_format

        try:
            a = int(gen[1])
            b = int(gen[3])
        except ValueError:
            return randomize_format
                
        if gen[2] != "to" or a > b:
            return randomize_format

        return f'`{random.randint(a,b)}`'

    gen = message.content.split()
    retval = inner_parse(gen)
    await message.channel.send(retval)

async def hello(message):
    await message.channel.send("Hello there, {0.mention}".format(message.author))