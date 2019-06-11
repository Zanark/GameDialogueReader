import pyscreenshot as pyss
import pytesseract as pyt
from PIL import Image
from gtts import gTTS
import os

img = pyss.grab(bbox=(0,600,1919,1060))
img.save('ss.png')
dialogue = pyt.image_to_string(img)
print(dialogue)

tts = gTTS(dialogue, lang='en')      #gTTS at work
tts.save('dOP.mp3')                #saving as mp3
os.system('mpg123 dOP.mp3')
os.system('rm dOP.mp3 ss.png')