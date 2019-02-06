import asyncio
import discord

# From API Reference https://discordpy.readthedocs.io/en/rewrite/api.html#client
async def thumb(client,message):
    """"""
    channel = message.channel
    await channel.send('Send me that 👍 reaction, mate')

    def check(reaction, user):
        return user == message.author and str(reaction.emoji) == '👍'

    try:
        await client.wait_for('reaction_add', timeout=60.0, check=check)
    except asyncio.TimeoutError:
        await channel.send('👎')
    else:
        await channel.send('👍')

    return

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

    await message.channel.send(f"{mentioned.mention}, you have 10 seconds to respond...")

    # Check if the mentioned user responded with key phrase
    def check(m):
        return (("test" in m.content.lower()
        or "my waves drippin" in m.content.lower()) 
        and m.channel == message.channel 
        and m.author == mentioned)

    try:
        await client.wait_for('message', timeout=10.0, check=check)
    except asyncio.TimeoutError:
        return f"{mentioned.mention} got no waves"
    else:
        return f"{mentioned.mention}'s waves DRIPPIN"

    return