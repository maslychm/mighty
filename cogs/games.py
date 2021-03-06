from discord.ext import commands
import discord
import asyncio
from cogs.utils import images

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="wavecheck")
    @commands.guild_only()
    async def wavecheck(self, ctx):
        
        """
        .wavecheck @mention
        Wavecheck somebody in the guild
        """

        if not ctx.message.mentions:
            return await ctx.send("Must mention a user")
        
        mentioned = ctx.message.mentions[0]
        m_str = mentioned.name
        if mentioned.nick is not None:
            m_str = mentioned.nick
        await ctx.send(f"{m_str}, you have 20 seconds to respond...")

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

    @commands.command(name='nuzzle')
    @commands.guild_only()
    async def nuzzle(self, ctx: commands.Context):
        
        """
        .nuzzle @mention
        *nuzzle* somebody in the guild
        """

        # Check for mentions, generate, send file
        if not ctx.message.mentions:
            return await ctx.send("Must _nuzzle_ a user by mentioning")
        
        mentioned = ctx.message.mentions[0]
        m_str = mentioned.name
        m_url = mentioned.avatar_url
        if mentioned.nick is not None:
            m_str = mentioned.nick

        a_str = ctx.message.author.name
        a_url = ctx.message.author.avatar_url
        if ctx.message.author.nick is not None:
            a_str = ctx.message.author.nick

        fpath = images.generate_nuzzle(a_str, m_str, a_url, m_url, reversed=False)
        await ctx.send(f"{m_str} gets _nuzzled_", file=discord.File(fpath))

        # Ask a user if they want to nuzzle back
        message_to_react = await ctx.send(f"{m_str}, _nuzzle_ them back? React to this message")
        await message_to_react.add_reaction("✅")
        await message_to_react.add_reaction("❌")

        # check() returns true if ✅ or ❌ reaction and ignore all other input
        # further assume one of two cases and only deal with positive
        def check(reaction, user):
            return (
                user == mentioned 
                and reaction.message.id == message_to_react.id
                and (str(reaction.emoji) == '✅' or str(reaction.emoji) == '❌')                    
            )

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            pass
        else:
            if str(reaction.emoji) == '✅':
                fpath = images.generate_nuzzle(m_str, a_str, a_url, m_url, reversed=True)
                await ctx.send(f"{a_str} was _nuzzled_ back", file=discord.File(fpath))
        finally:
            await message_to_react.delete()
