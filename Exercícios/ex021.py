# Tocando um MP3
from emoji import emojize
from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
input(emojize('Toca um som aí! :headphones:', use_aliases=True))