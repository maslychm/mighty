# Main driver for the BOT. Start client, receive messages

import discord
import asyncio
import credentials
from processmessage import detect_command
from plugins import onjoin

class MightyBOT(discord.Client):

	async def on_message(self, message):
		if message.author == self.user:
			return

		await detect_command(client, message)
		return

	async def on_member_join(self, member):
		await onjoin.onjoin_welcome(client,member)
		return

	async def on_member_remove(self,member):
		await onjoin.on_leave(client,member)
		return
			
	async def on_ready(self):
		print('Logged in as')
		print(self.user.name)
		print(self.user.id)
		print('------')

client = MightyBOT()
client.run(credentials.TOKEN)