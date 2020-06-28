from discord.ext import commands
from discord import Embed
from datetime import date
import calendar

class Administration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.helpmsg_guild_dict = {}
        self.helpmsg2_guild_dict = {}
        self.botinfo_guild_dict = {}
        # FIXME make the shits delete themselves

    @commands.command(name='close')
    @commands.is_owner()
    async def close(self, ctx: commands.Context):
        """Close the Bot client"""
        await ctx.channel.send("admin: shutting down...")
        await self.bot.close()

    @commands.command(name='checkowner')
    async def checkowner(self, ctx: commands.Context):
        """Check if user is a bot owner"""
        isowner = await self.bot.is_owner(ctx.message.author)
        if isowner:
            await ctx.channel.send("admin: you're an owner")
        else:
            await ctx.send("admin: you're not an owner")

    @commands.cooldown(rate=2, per=15, type=commands.BucketType.guild)
    @commands.command(name='serverinfo', aliases=['info'])
    async def serverinfo(self, ctx: commands.Context):
        """Display detailed server info"""
        gd_nam = ctx.guild.name
        gd_mnum = ctx.guild.member_count
        gd_owner_id = ctx.guild.owner_id
        gd_owner = ctx.guild.get_member(gd_owner_id)
        
        now = date.today()
        mon = calendar.month_name[now.month]

        infoholder = [
            f"Guild Name : {gd_nam} ",
            "---------------------------",
            f"< Owner    : {gd_owner} >",
            f"< Members  : {gd_mnum} >",
            f"< As of    : {mon} {now.day} of {now.year} >",
        ]

        ret = "```md\n" + "\n".join(infoholder) + "```"

        await ctx.send(ret)

    @commands.cooldown(rate=3, per=5, type=commands.BucketType.guild)
    @commands.command(name='botinfo', aliases=['bot'])
    async def botinfo(self, ctx: commands.Context):
        """Display Bot info"""
        msg = '''
        Written by mighty_lord#4526
        https://github.com/maslychm/mighty
        '''
        await ctx.send(msg)

    @commands.cooldown(rate=2, per=15, type=commands.BucketType.member)
    @commands.command(name='help', aliases=['commands'])
    async def help(self, ctx: commands.Context):
        """Display commonly used commands"""
        embedded = Embed(title='Help Page 1', color=0x44DC26)
        embedded.add_field(name='play <YT Link>', value='Play music from YouTube', inline=False)
        embedded.add_field(name="wavecheck", value="got waves?", inline = False)
        embedded.add_field(name='help2', value='Help page 2', inline=False)

        await ctx.send(embed=embedded)

    @commands.cooldown(rate=2, per=15, type=commands.BucketType.member)
    @commands.command(name='help2', aliases=['commands2'])
    async def help2(self, ctx: commands.Context):
        """Display less frequently used commands"""
        embedded = Embed(title='Help Page 2', color=0x44DC26)
        embedded.add_field(name="help",value="Display Help Menu",inline = False)
        embedded.add_field(name="serverinfo", value="Display detailed server info", inline = False)
        embedded.add_field(name="botinfo", value="More information about MightyBOT", inline = False)

        await ctx.send(embed=embedded)
