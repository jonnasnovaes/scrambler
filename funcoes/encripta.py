import string
from random import random

def encripta():

y = ""

    for i in range(0, 3):
        y = y  +  random.choice(string.ascii_letters)


        return y