# Main driver for the BOT. Start client, receive messages

import discord
import asyncio
import credentials
from processmessage import detect_command

class MightyBOT(discord.Client):

	async def on_message(self, message):
		# Don't reply to yourself
		if message.author == self.user:
			return

		# Parse message
		await detect_command(client, message)
		return
			
	async def on_ready(self):
		print('Logged in as')
		print(self.user.name)
		print(self.user.id)
		print('------')

client = MightyBOT()
client.run(credentials.TOKEN)