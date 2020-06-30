from PIL import Image, ImageFont, ImageDraw
import requests
from io import BytesIO
import os

MAXPICSIZE = 300

def generate_onjoin_pic(namestr: str, member_id: int, url):
    """
    Generates an image with user name and image
    and retuns the absolute path to the file
    """

    # Check if dir exists
    if not os.path.isdir(os.getcwd() + "/temp/"):
        os.mkdir(os.getcwd() + "/temp/")
        print("making dir here")

    # Set up return path
    retpath = "temp/w" + str(member_id) + ".png"

    # Open template and font
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
    im.save(retpath)

    return retpath

def generate_hat(member_id, url=None):

    if url == None:
        return

    # Check if dir exists
    if not os.path.isdir(os.getcwd() + "/temp/"):
        os.mkdir(os.getcwd() + "/temp/")
        print("making dir here")

    # Set up return path
    retpath = "temp/h" + str(member_id) + ".png"

    # Download image
    response = requests.get(url)
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
    imageBG.save(retpath)

    return retpath


def generate_nuzzle(a, m, reversed=False):
    nuzzlestr = a + " *nuzzles* " + m
    print(nuzzlestr)
    retpath = "fpath"

    # Check if dir exists
    if not os.path.isdir(os.getcwd() + "/temp/"):
        os.mkdir(os.getcwd() + "/temp/")
        print("making dir here")

    # Set up return path
    retpath = "temp/n" + a + "_" + m + ".png"

    # Open template and font
    impath = "resources/nuzzle_template.jpeg"
    if reversed:
        impath = "resources/nuzzle_template_reversed.jpeg"

    im = Image.open(impath)
    font_type = ImageFont.truetype("resources/PlayfairDisplaySC-Bold.otf",32)

    draw = ImageDraw.Draw(im)
    draw.text(xy=(50,240),text=nuzzlestr,fill=(17,17,19),font=font_type)
    im.save(retpath)

    return retpath
