# Plugin for my own testing and learning API

def logging(client):
    print('Here goes logging')

    allguilds = client.guilds
    print(allguilds)
    
    currentguild = allguilds[0]
    print(currentguild)
#    members = currentguild.members
#    print(members)
    owner = currentguild.owner
    print(owner)
    print('-----')
    print(currentguild.member_count)

    return