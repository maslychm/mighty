from PIL import Image, ImageFont, ImageDraw
import discord
import os 

# FIXME Poorly writte, yet to be worked on 
def generate_onjoin_pic(username):
    # Get and print current working directory
    #cwd = os.getcwd()
    #print(cwd)

    # Open image file and font file
    im = Image.open("plugins/template.PNG")
    font_type = ImageFont.truetype("plugins/PlayfairDisplaySC-Bold.otf",39)

    # Add text user name to image
    draw = ImageDraw.Draw(im)
    draw.text(xy=(185,70),text=username,fill=(17,17,19),font=font_type)
    #im.show()
    im.save("tmp/temp.png")
    return "tmp/temp.png"

# For now to test just reply into user's DM
async def test_welcome(client,message):

    #channel = discord.Guild.get_channel(491900012104646668)
    
    # Get the string of user name
    user = message.author
    if isinstance(user,discord.Member):
        username = user.nick
    else: 
        username = user.name
    print(username)
    toEmbed = generate_onjoin_pic(username)
    await message.channel.send(file=discord.File(toEmbed))
    return

if __name__ == "__main__":
    welcome_message("client","mighty_lord")