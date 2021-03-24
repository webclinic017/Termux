#!python

# gTTS TXT File to MP3

import os
from gtts import gTTS
from glob import glob

for f in glob("*.txt"):
	with open(f) as file:
		t = gTTS(file.read(), "en")
	t.save(os.path.splitext(f)[0] + ".mp3")

for f in glob("*.mp3"):
	os.startfile(f)
