import discord
from datetime import datetime, date
import holidays
import calendar

async def serverinfo(message):
    if not isinstance(message.channel, discord.TextChannel):
        return
    guild = message.guild
    guildname = guild.name
    membernum = guild.member_count
    now = datetime.today()
    month = calendar.month_name[now.month]

    ret = f"As of {month} {now.day} of {now.year} **{guildname}** has {membernum} members"

    us_holidays = holidays.UnitedStates()
    nowstr = now.strftime("%m-%d-%Y")

    if nowstr in us_holidays:
        ret += "\nAlso, today is {}".format(us_holidays.get(nowstr))

    await message.channel.send(ret)

async def botinfo(message):
    msg = '''
    Written by mighty_lord#4526
    https://github.com/maslychm/mighty
    '''
    await message.channel.send(msg)

async def helpfunc(message):
    msg = '**AVAILABLE COMMANDS:**'
    embedded = discord.Embed(color=0x44DC26)

    embedded.add_field(
        name="!help",
        value="Display Help Menu",
        inline = False
    )
    embedded.add_field(
        name="!test",
        value="Count your messages in current channel (up to 100)",
        inline = False
    )
    embedded.add_field(
        name="!random",
        value="Generate a random number !random a to b",
        inline = False
    )
    embedded.add_field(
        name="!users or !serverinfo",
        value="Display number of users in the channel",
        inline = False
    )
    embedded.add_field(
        name="!wavecheck",
        value="got waves?",
        inline = False
    )
    embedded.add_field(
        name="!roll",
        value="Roll a dice",
        inline = False
    )
    embedded.add_field(
        name="!gentest",
        value="Test welcome image generation",
        inline=False
    )
    embedded.add_field(
        name="!botinfo",
        value="More information about MightyBOT",
        inline = False
    )

    await message.channel.send(msg,embed=embedded)

async def linkVoiceStream(message):
    if (isinstance(message.channel, discord.DMChannel)
    or message.author.voice is None):
        return await message.channel.send("Join a Voice Chat on Server")
    
    vcID = message.author.voice.channel.id
    gID = message.guild.id
    ret = """Click on link for screen share: 
    http://www.discordapp.com/channels/{}/{}""".format(gID, vcID)
    await message.channel.send(ret)