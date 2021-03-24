#!python

# Combine TXT Files to a MP3

import os
from gtts import gTTS
from glob import glob

t = ""
for f in glob("*.txt"):
	with open(f) as file:
		t += file.read()
tts = gTTS(t, "en")
name = "full.mp3"
tts.save(name)
os.startfile(name)
