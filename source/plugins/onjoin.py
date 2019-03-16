from PIL import Image, ImageFont, ImageDraw
import discord
import os
import requests
from io import BytesIO

def generate_onjoin_pic(namestr,url):
    # Get and print current working directory
    
    # Debug:
    #cwd = os.getcwd()
    #print(cwd)

    # Open image file and font file
    im = Image.open("plugins/template.PNG")
    font_type = ImageFont.truetype("plugins/PlayfairDisplaySC-Bold.otf",39)

    # Get and resize user avatar from url
    response = requests.get(url)
    avatar = Image.open(BytesIO(response.content))
    avatar.thumbnail((64,64), Image.ANTIALIAS)

    # Add text user name to image
    draw = ImageDraw.Draw(im)
    draw.text(xy=(185,70),text=namestr,fill=(17,17,19),font=font_type)
    im.paste(avatar,box=(5,5))
    im.save("tmp/temp.png")
    return "tmp/temp.png"

async def onjoin_welcome(client,member):
    channel = client.get_channel(491900012104646668)
    namestr = member.name
    if (member.nick):
        namestr = member.nick
    image = generate_onjoin_pic(namestr,member.avatar_url)
    await channel.send(file=discord.File(image))
    return

async def on_leave(client,member):
    channel = client.get_channel(491900012104646668)
    namestr = member.name
    if (member.nick):
        namestr = member.nick
    await channel.send(f"{member.name}, has left us")
    return
    
async def test_welcome(client,message):

    # For debug only
    if isinstance(message,str):
        namestr = message
        image = generate_onjoin_pic(namestr,"")
        return

    # Check if channel is DM or whitelisted
    WHITELIST = [491899563527897089,491900012104646668]
    if not (isinstance(message.channel,discord.DMChannel)
    or message.channel.id in WHITELIST):
        return

    # Get user name string
    namestr = message.author.name
    if (message.author.nick):
        namestr = message.author.nick

    image = generate_onjoin_pic(namestr,message.author.avatar_url)
    await message.channel.send(file=discord.File(image))
    return

if __name__ == "__main__":
    test_welcome("client","mighty_lord")