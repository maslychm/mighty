import datetime
from discord.ext import commands
from credentials import TOKEN as TOKEN
from cogs import admin, api, games, join, music

description = '''
Bot for servers mighty likes :)
'''

class MightyBot(commands.Bot):
    async def on_ready(self):
        print(f'Started: {datetime.datetime.now()}')
        print(f'Ready: {self.user} (ID: {self.user.id})')

bot = MightyBot(
    command_prefix=commands.when_mentioned_or('.'), 
    description=description,
    # owner_id=232346727221297164,
    )

bot.add_cog(admin.Administration(bot))
bot.add_cog(api.API(bot))
bot.add_cog(games.Games(bot))
bot.add_cog(join.JoinLeave(bot))
bot.add_cog(music.Music(bot))
bot.run(TOKEN)