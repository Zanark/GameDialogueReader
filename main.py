import pyscreenshot as pyss
import pytesseract as pyt
from PIL import Image
import PIL.ImageOps
from gtts import gTTS
import os

# img = pyss.grab(bbox=(0,750,1919,1060))
# img.save('ss.png')

img = Image.open('/home/zanark/Pictures/ss.png').convert('L')
img = img.convert('RGB')
PIL.ImageOps.invert(img)
img.save("/home/zanark/ss.jpg", dpi=(10000,10000))
img = Image.open('/home/zanark/ss.png')

dialogue = pyt.image_to_string(img, lang='eng', config='--psm 12')
print(dialogue)

tts = gTTS(dialogue, lang='en')      #gTTS at work
tts.save('dOP.mp3')                #saving as mp3
os.system('mpg123 dOP.mp3')
#os.system('rm dOP.mp3 ss.png')