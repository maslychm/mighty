import discord
import processmessage
import modules.joinrelated as onjoin

from credentials import TOKEN as TOKEN

ADMIN_ID = 232346727221297164

class Mighty(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        if message.content.startswith("close") and message.author.id == ADMIN_ID:
            await message.channel.send("shutting down...")
            await client.close()

        if message.author.bot:
            return

        await processmessage.detect_command(self, message)

    async def on_member_join(self, member):
        await onjoin.onjoin_welcome(client,member)

    async def on_member_remove(self,member):
        await onjoin.on_leave(client,member)

client = Mighty()
client.run(TOKEN)