from discord.ext import commands
from cogs.utils import images
import discord

class API(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='test_join', aliases=['gentest'])
    async def test_join(self, ctx):

        """Generate onjoin image"""

        namestr = ctx.message.author.name
        member_id = ctx.message.author.id
        img_url = ctx.message.author.avatar_url
        
        # Get user name string
        namestr = ctx.message.author.name
        if hasattr(ctx.message.author,"nick"):
            if ctx.message.author.nick is not None:
                if ctx.message.author.nick:
                    namestr = ctx.message.author.nick

        fpath = images.generate_onjoin_pic(namestr, member_id, img_url)
        await ctx.send(file=discord.File(fpath))

    @commands.command(name='test_hat', aliases=['genhat'])
    async def test_hat(self, ctx):

        """Generate image with a chrismas hat"""
    
        member_id = ctx.message.author.id

        # Backgroud in the following priority: Attachment, Mentioned Avatar, Mentionee Avatar
        background_url = ctx.message.author.avatar_url

        if ctx.message.attachments:
            if ctx.message.attachments[0].url.lower().endswith((".jpg",".jpeg",".png")):
                background_url =  ctx.message.attachments[0].url
            else:
                return await ctx.send("Attachment has to be an image")

        elif ctx.message.mentions:
            targetUser = ctx.message.mentions[0]
            background_url = targetUser.avatar_url

        fpath = images.generate_hat(member_id, background_url)

        if fpath == None:
            ctx.send("Could not get the image for some reason")
            return

        await ctx.send(file=discord.File(fpath))
        
            