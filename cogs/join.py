from discord.ext import commands
from cogs.utils import images
import discord

class JoinLeave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        namestr = member.name
        member_id = member.id
        img_url = member.avatar_url
        if channel is not None:
            # await channel.send(f'Welcome {member.mention}.')
            fpath = images.generate_onjoin_pic(namestr, member_id, img_url)
            return await channel.send(file=discord.File(fpath))

    # No way to deal universally with leaves on many servers
    # so will be left undealt with for now
    # @commands.Cog.listener()
    # async def on_member_remove(self, member):
    #     channel = self.bot.get_user(232346727221297164)
    #     if channel is not None:
    #         await channel.send(f"{member.name} left {member.guild.name}")
