import pyscreenshot as pyss
import pytesseract as pyt
from PIL import Image, ImageEnhance
import PIL.ImageOps
from gtts import gTTS
import os

img = pyss.grab(bbox=(5,780,1910,1060))
img.save('ss.png')
img = Image.open('ss.png').convert('L')
img=PIL.ImageOps.invert(img)
img = ImageEnhance.Contrast(img).enhance(2.0)
img = ImageEnhance.Sharpness(img).enhance(2.0)
img.save("ss.jpg", dpi=(10000,10000))
img = Image.open('ss.jpg')

dialogue = pyt.image_to_string(img, lang='eng', config='--psm 12')
print(dialogue)

tts = gTTS(dialogue, lang='en')      #gTTS at work
tts.save('dOP.mp3')                #saving as mp3
os.system('mpg123 dOP.mp3')
os.system('rm dOP.mp3 ss.png ss.jpg')
