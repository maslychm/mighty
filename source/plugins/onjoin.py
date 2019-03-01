from PIL import Image, ImageFont, ImageDraw

im = Image.open("template.PNG")
font_type = ImageFont.truetype("black.ttf",40)

draw = ImageDraw.Draw(im)
draw.text(xy=(100,100),text="Hello there!",fill=(17,61,193),font=font_type)
im.show()