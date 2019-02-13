# Embedded !help menu

import discord

async def helps(client,message):
    msg = 'avaliable commands:\n' + \
        '`!help` `!test` `!info` `!hello` `!random` `!users`' + \
        '\n`!serverinfo` `!wavecheck` `!roll` `!thumb`'

    embedded = discord.Embed(color=0x44DC26)

    embedded.add_field(
        name="!info",
        value="More information about MightyBOT",
        inline = False
    )

    embedded.add_field(
        name="!help",
        value="Display Help Menu",
        inline = False
    )

    embedded.add_field(
        name="!test",
        value="Count your messages in current channel (up to 100)",
        inline = False
    )

    embedded.add_field(
        name="!random",
        value="Generate a random bumber !random a to b",
        inline = False
    )

    embedded.add_field(
        name="!users or !serverinfo",
        value="Display number of users in the channel",
        inline = False
    )

    embedded.add_field(
        name="!wavecheck",
        value="got waves?",
        inline = False
    )

    embedded.add_field(
        name="!roll",
        value="Roll a dice",
        inline = False
    )

    await message.channel.send(msg,embed=embedded)

    return