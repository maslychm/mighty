from PIL import Image, ImageFont, ImageDraw
import discord
import os
import requests
from io import BytesIO

MAXPICSIZE = 300
IMAGES_ALLOWED_LIST = [491899563527897089,491900012104646668,652345677942358026]
JOIN_LEAVE_NOTIF_CHANNEL = 491900012104646668
TEMP_WELCOME_PATH = "temp/tempImg.png"
TEMP_HAT_PATH = "temp/temphat.png"

def generate_onjoin_pic(namestr,url):
    # Open image file and font file
    im = Image.open("resources/template.PNG")
    font_type = ImageFont.truetype("resources/PlayfairDisplaySC-Bold.otf",39)

    # Get and resize user imageBG from url
    response = requests.get(url)
    imageBG = Image.open(BytesIO(response.content))
    imageBG.thumbnail((64,64), Image.ANTIALIAS)

    # Add text user name to image
    draw = ImageDraw.Draw(im)
    draw.text(xy=(185,70),text=namestr,fill=(17,17,19),font=font_type)
    im.paste(imageBG,box=(5,5))
    im.save(TEMP_WELCOME_PATH)

async def onjoin_welcome(client,member):
    channel = client.get_channel(JOIN_LEAVE_NOTIF_CHANNEL)
    namestr = member.name
    if (member.nick):
        namestr = member.nick
    generate_onjoin_pic(namestr,member.avatar_url)
    return await channel.send(file=discord.File(TEMP_WELCOME_PATH))

async def on_leave(client,member):
    channel = client.get_channel(JOIN_LEAVE_NOTIF_CHANNEL)
    namestr = member.name
    if (member.nick):
        namestr = member.nick
    return await channel.send(f"{namestr} left the channel")

async def generate_hat(client,message):

    if not is_whitelisted(message):
        return

    imageBG = None
    
    if message.attachments:
        if message.attachments[0].url.lower().endswith((".jpg",".jpeg",".png")):
            response = requests.get(message.attachments[0].url)
            imageBG = Image.open(BytesIO(response.content))
        else:
            return await message.channel.send("Attachment has to be an image")

    elif message.mentions:
        targetUser = message.mentions[0]
        response = requests.get(targetUser.avatar_url)
        imageBG = Image.open(BytesIO(response.content))
        
    else:
        response = requests.get(message.author.avatar_url)
        imageBG = Image.open(BytesIO(response.content))
    
    bg_w, bg_h = imageBG.size

    # Get hat from resources
    hatImg = Image.open('resources/Hat.png')
    hat_w, hat_h = hatImg.size
    
    # Check if imageBG is too small and resize hat to 3:2
    if bg_w < MAXPICSIZE or bg_h < MAXPICSIZE:
        hatImg.thumbnail((bg_w / 3 * 2, bg_h / 3 * 2), Image.ANTIALIAS)
        hat_w, hat_h = hatImg.size
    else:
        imageBG.thumbnail((MAXPICSIZE, MAXPICSIZE), Image.ANTIALIAS)
        bg_w, bg_h = imageBG.size

    # Paste hat on correct offsets
    offset = ((bg_w - hat_w), 0)
    imageBG.paste(hatImg, offset, mask=hatImg)
    imageBG.save(TEMP_HAT_PATH)
    
    return await message.channel.send(file=discord.File(TEMP_HAT_PATH))
    
async def test_welcome(client,message):

    if not is_whitelisted(message):
        return

    # Get user name string
    namestr = message.author.name
    if hasattr(message.author,"nick"):
        if message.author.nick is not None:
            if message.author.nick:
                namestr = message.author.nick

    generate_onjoin_pic(namestr,message.author.avatar_url)
    return await message.channel.send(file=discord.File(TEMP_WELCOME_PATH))

def is_whitelisted(message):
    if not (isinstance(message.channel,discord.DMChannel)
    or message.channel.id in IMAGES_ALLOWED_LIST):
        return False
    return True