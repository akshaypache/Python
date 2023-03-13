from PIL import ImageFont
font = ImageFont.truetype('times.ttf', 12)
size = font.getsize('Aadesh Lokhande')
print(size)