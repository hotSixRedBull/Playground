# ref = https://www.youtube.com/watch?v=bf_UOFFaHiY&index=7&list=PL-j31rK7baSnfLYWEw5kPK4xC6RPk7NU-

from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class Cordinates():
    replayBtn = (480,400)
    dinasaur = (245,395)
    #280,420


def restartGame():
    pyautogui.click(Cordinates.replayBtn)

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("Jump")
    pyautogui.keyUp('space')

def imageGrab():
    box = (Cordinates.dinasaur[0]+60,Cordinates.dinasaur[1],Cordinates.dinasaur[0]+100,Cordinates.dinasaur[1]+30)
    image = ImageGrab.grab(box)
    greyImage = ImageOps.grayscale(image)
    a = array(greyImage.getcolors())
    print(a.sum())

def main():
    restartGame()
    while True:
        if (imageGrab()!=1447):
            pressSpace()
            time.sleep(0.1)             

main()