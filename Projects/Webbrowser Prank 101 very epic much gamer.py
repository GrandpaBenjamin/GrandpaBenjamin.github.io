#Webbrowser prank! :)

import webbrowser
from random import randint
import time
import sys

x = 10
def interval():
    while True:
        time.sleep(randint(300,600))
        webbrowser.open('https://www.youtube.com/watch?v=iFzncBVM9Js')

def spam():
    while True:
        time.sleep(0)
        webbrowser.open('https://www.youtube.com/watch?v=iFzncBVM9Js')

def kill():
    quit()
def countdown(x):
    while True:
        time.sleep(1)
        x = x - 1
        print("You have", x, "seconds until spam!")
        if x <= 0:
            print("Spam has begun")
            spam()
            break

