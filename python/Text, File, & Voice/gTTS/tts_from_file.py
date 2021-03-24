import os
from gtts import gTTS

with open("text.txt") as file:
	t = gTTS(file.read(), "en")
t.save("text.mp3")

os.startfile("text.mp3")
