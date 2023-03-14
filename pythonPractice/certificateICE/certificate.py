from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def AddImg(h,w,x=94,y=274):
    im = Image.open(r"logo.png")
    im1 = im.resize((h,w))
    im1.save("resize.png")
    img1 = Image.open(r"abc1.png")
    img2 = Image.open(r"resize.png",)
    img1.paste(img2, (x,y), mask = img2)
    img1.save("abc1.png")

def WriteText(text,y,fileName="abc1.png",fontsize=23,x=True):
    img = Image.open(fileName)
    I1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('oswald/Oswald-Bold.ttf', fontsize)
    if x==True:
        size = myFont.getsize(text)
        x = 360-size[0]//2
    I1.text((x, y), text=text,font=myFont, fill =(0, 0, 0))
    img.save("abc1.png")


WriteText("Authorized Training Center",280,"certificate.jpg")
WriteText("ICE COMPUTERS",310)
WriteText("Wanadongri",335)
WriteText("This is to certify that",460,fontsize=18)
WriteText("Aadesh Gautam Lokhande",495,fontsize=18)
WriteText("has successfully completed",530,fontsize=18)
WriteText("Certificate course in Python",565,fontsize=18)
WriteText("from 31/01/2000 to 30/03/2000",600,fontsize=18)
WriteText('And has passed the examination with "A++" Grade',630,fontsize=18)

WriteText("certificate Number",690,fontsize=14)
WriteText("2000010001",710,fontsize=14)
WriteText("Date : 10/04/2000",730,fontsize=14)

WriteText("APC",385,x=125,fontsize=18)
WriteText("MH4023001",405,x=110, fontsize=14)


AddImg(94,94,x=94,y=274)
AddImg(126,55,x=114,y=685)
AddImg(94,94,x=526,y=272)
AddImg(94,50,x=526,y=379)
