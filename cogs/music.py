from discord.ext import commands

class TestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hello2')
    async def hello2(self, ctx: commands.Context):
        print("does it ever get here")
        await ctx.send("testing building in cogs2")