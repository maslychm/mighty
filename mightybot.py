import datetime
from discord.ext import commands
from credentials import TOKEN as TOKEN
from cogs import admin

description = '''
Bot for servers mighty likes :)
'''

class MightyBot(commands.Bot):
    async def on_ready(self):
        print(f'Started: {datetime.datetime.now()}')
        print(f'Ready: {self.user} (ID: {self.user.id})')

    async def on_member_join(self, ctx):
        pass
        #FIXME

    async def on_member_remove(self, ctx):
        pass
        #FIXME


bot = MightyBot(
    command_prefix=commands.when_mentioned_or('.'), 
    description=description,
    # owner_id=232346727221297164,
    )

# bot.add_cog(TestCog(bot))
bot.add_cog(admin.Administration(bot))
bot.run(TOKEN)