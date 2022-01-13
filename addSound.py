#Added to GitHub
import playsound
from pygame import mixer
import time

mixer.init()
sound1 = mixer.Sound("birds.mp3")
sound2 = mixer.Sound("frogs.mp3")

#mixer.music.load("frogs.mp3")

mixer.Channel(0).play(sound2)
time.sleep(3)
mixer.Channel(1).play(sound2)
answer = input("What is your name?")
mixer.music.stop()
print ("Hello, how are you?")

time.sleep(5)
mixer.music.play()
input()

# playsound.playsound("frogs.mp3", block=False)
# print ("I love frogs")
# answer = input("Type any key") 