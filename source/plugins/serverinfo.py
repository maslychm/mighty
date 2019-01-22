# Print information about the server

def serverinfo(client, message):

    guild = message.guild
    guildname = guild.name
    membernum = guild.member_count

    return f"**{guildname} currently has {membernum} members**"
