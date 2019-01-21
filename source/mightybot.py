import discord
import asyncio
import credentials
from processmessage import detect_command

class MyClient(discord.Client):

	async def on_message(self, message):
		# Don't reply to yourself
		if message.author == self.user:
			return

		# Parse message
		await detect_command(message)
		return
			
	async def on_ready(self):
		print('Logged in as')
		print(self.user.name)
		print(self.user.id)
		print('------')

client = MyClient()
client.run(credentials.TOKEN)