# This is a program to take an input from a user
# and then display it letter for letter with a little sound when each letter is displayed.
import simpleaudio
import time
import os


text = input("Hi! Please input your text")
length = len(text)
location = 0
os.system('clear')
text = text.strip() #delete line breaks

while location < length:
    wave_obj = simpleaudio.WaveObject.from_wave_file("bell.wav")
    play_obj = wave_obj.play()
    #play_obj.wait_done()
    time.sleep(0.06)
    print(text[location], end="")

    if text[location] == ",":
        time.sleep(0.5)
    if text[location] == ".":
        time.sleep(1)
    if text[location] == "/n":
        print ("ERROR on NEWLINE")

    location += 1