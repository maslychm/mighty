import discord
import asyncio
import credentials
import random

class MyClient(discord.Client):

	async def on_message(self, message):
		# Don't reply to yourself
		if message.author == self.user:
			return
			
		if message.content.startswith('!test'):
			counter = 0
			tmp = await message.channel.send('Calculating messages...')
			async for msg in message.channel.history(limit=100):
				if msg.author == message.author:
					counter += 1
			await tmp.edit(content='You have {} messages.'.format(counter))

		if message.content.startswith('!hello'):
			await message.channel.send(f'Hello {message.author.mention}')

		if message.content.startswith('!info'):
			msg = 'Written by mighty_lord#4526\n'
			await message.channel.send(msg)

		if message.content.startswith('!help'):
			msg = 'avaliable commands:\n' + \
				'`!help` `!test` `!info` `!hello` `!random`'
			await message.channel.send(msg)

		if message.content.startswith('!hewwo :3'):
			msg = 'Ayy you found an eastern egg `nuzzles`'
			await message.channel.send(msg)

		if message.content.startswith("!random"):
			# FIXME THIS IS GETTING TOO LONG TO PARSE,
			# MAKE INTO PLUGIN AND PARSE FOR ERRORS IN ORDER
			random_format = "-\nIncorrect format\n" + \
					"use `!random a to b`\n" + \
					"where a and b are numbers and a < b"

			gen = message.content.split()
			
			if len(gen) == 1:
				await message.channel.send(random.randint(0,100))
				return
			if len(gen) < 4:
				await message.channel.send(random_format)
				return

			try:
				a = int(gen[1])
				b = int(gen[3])
			except ValueError:
				await message.channel.send(random_format)
				return
				
			if gen[2] != "to" or a > b:
				await message.channel.send(random_format)
				return

			await message.channel.send(f'`{random.randint(a,b)}`')
			
		if message.content.startswith('!roll'):
			await message.channel.send(f"`{random.randint(0,6)}`")
			return
			
		return
			
	async def on_ready(self):
		print('Logged in as')
		print(self.user.name)
		print(self.user.id)
		print('------')

client = MyClient()
client.run(credentials.TOKEN)