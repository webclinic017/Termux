#!python

# gTTS-MP3-for-Every-Line-in-TXT-File.py

import os
from gtts import gTTS
from glob import glob

lst = []

with open("number.txt") as file:
	for n,line in enumerate(file):
		tts = gTTS(line,"en")
		name = "number" + str(n) + ".mp3"
		tts.save(name)
		lst.append(name) # this is just to hear them with os....

[os.startfile(name) for name in lst]
