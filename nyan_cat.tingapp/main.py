import tingbot
from tingbot import *

nyan_cat = Image.load('nyancat.gif')

def loop():
    screen.image(nyan_cat)

tingbot.run(loop)
