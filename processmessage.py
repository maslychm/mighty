import discord
import modules.joinrelated as jn
import modules.userrelated as usr
import modules.guildrelated as gd

commandList = {
    "!test" : usr.test,
    "!list" : gd.helpfunc,
    "!help" : gd.helpfunc,
    "!random" : usr.randomize,
    "!serverinfo" : gd.serverinfo,
    "!users" : gd.serverinfo,
    "!botinfo" : gd.botinfo,
    "!hello" : usr.hello,
    "!link" : gd.linkVoiceStream,
}

# Need a cliend argument passed
commandList2 = {
    "!thumb" : usr.thumb,
    "!wavecheck" : usr.wavecheck,
    "!gentest" : jn.test_welcome,
}

async def detect_command(client, message):
    for comm, func in commandList.items():
        if comm in message.content:
            return await func(message)

    for comm, func in commandList2.items():
        if comm in message.content:
            return await func(client, message)
