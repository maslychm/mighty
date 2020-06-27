from discord.ext import commands

class Administration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='close')
    async def close(self, ctx: commands.Context):
        isowner = await self.bot.is_owner(ctx.message.author)
        if isowner:
            await ctx.channel.send("admin: shutting down...")
            await self.bot.close()

    @commands.command(name='checkowner')
    async def checkadmin(self, ctx: commands.Context):
        isowner = await self.bot.is_owner(ctx.message.author)
        if isowner:
            await ctx.channel.send("admin: you're an owner")
        else:
            await ctx.send("admin: you're not an owner")