from discord.ext import commands
import asyncio

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="wavecheck")
    @commands.guild_only()
    async def wavecheck(self, ctx):
        """
        !wavecheck @mention
        Wavecheck somebody in 3+ users channel
        Only the first user on the mention list will be checked
        """

        if not ctx.message.mentions:
            return await ctx.send("Must mention a user")
        
        mentioned = ctx.message.mentions[0]
        await ctx.send(f"{mentioned.mention}, you have 20 seconds to respond...")

        # Check if the mentioned user responded with key phrase
        def check(m):
            return (("test" in m.content.lower()
            or "my waves drippin" in m.content.lower()) 
            and m.channel == ctx.message.channel 
            and m.author == mentioned)

        try:
            await self.bot.wait_for('message', timeout=20.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send(f"{mentioned.mention} got no waves")
        else:
            await ctx.send(f"{mentioned.mention}'s waves DRIPPIN")

