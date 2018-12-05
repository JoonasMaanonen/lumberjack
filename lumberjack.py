from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pynput.keyboard import Key, Controller
from PIL import Image
import argparse
import shutil
import os
from time import sleep

# Position of the trees, manually fetched with GIMP
sameSideRightPixelCoords = (234, 99)
sameSideLeftPixelCoords = (65, 97)
diffSideLeftPixelCoords = (65, 146)
diffSideRightPixelCoords = (234, 146)

bushColor = (126, 173, 79) # Color of the tree

# Setup selenium
keyboard = Controller()
game = webdriver.Firefox()
# URL of the game
url = "https://tbot.xyz/lumber/#eyJ1Ijo2MjMyMzE0MCwibiI6Ikpvb25hcyBNYWFub25lbiIsImciOiJMdW1iZXJKYWNrIiwiY2kiOiItNTgzNzgwOTE4ODMwNzY1MDg2NCIsImkiOiJCQUFBQUpJUkFRQzlLQXJBcWwwOXlEQ3RUeWMifTEwMzkxYTE2Yjg5YzA4ZDliNzlhM2JjZjg0YTU1YjEw?tgShareScoreUrl=tg%3A%2F%2Fshare_game_score%3Fhash%3DVS-S_vCC9se7WCsAa398S9pLU2trqi3GXbEZ4oUfTEM"
game.get(url)
game.set_window_size(300, 500)

def firstThreeInputs():
    lastPress = ""
    for i in range(3):
        game.save_screenshot('images/lumberjack' + '_first' + '.png')
        im = Image.open('images/lumberjack' +  '_first' + '.png')
        sameRightPixel = im.getpixel(sameSideRightPixelCoords)[0:3]
        sameLeftPixel = im.getpixel(sameSideLeftPixelCoords)[0:3]
        diffRightPixel = im.getpixel(diffSideRightPixelCoords)[0:3]
        diffLeftPixel = im.getpixel(diffSideLeftPixelCoords)[0:3]
        if(sameRightPixel == bushColor or diffRightPixel == bushColor):
            lastPress = "left"
            pressLeft()
        elif(sameLeftPixel == bushColor or diffLeftPixel == bushColor):
            lastPress = "right"
            pressRight()
        else:
            if lastPress == "left":
                pressLeft()
            else:
                pressRight()

def naiveBot():
    id = 1
    while(1):
        game.save_screenshot('images/lumberjack' + str(id) + '.png')
        im = Image.open('images/lumberjack' + str(id) + '.png')
        sameRightPixel = im.getpixel(sameSideRightPixelCoords)[0:3]
        sameLeftPixel = im.getpixel(sameSideLeftPixelCoords)[0:3]
        diffRightPixel = im.getpixel(diffSideRightPixelCoords)[0:3]
        diffLeftPixel = im.getpixel(diffSideLeftPixelCoords)[0:3]
        if sameRightPixel == bushColor or diffRightPixel == bushColor:
            pressLeft()
        elif (sameLeftPixel == bushColor or diffLeftPixel == bushColor):
            pressRight()
        else:
            pass
        id += 1
        sleep(0.15)

def pressLeft():
    keyboard.press(Key.left)
    keyboard.release(Key.left)

def pressRight():
    keyboard.press(Key.right)
    keyboard.release(Key.right)

def main():
    try:
        if not os.path.exists("images"):
            os.makedirs("images")
        else:
            print("images dir already exists!")
        input("Press Enter to start the script!")
        print("Sleep 5 seconds to change main screen")
        sleep(5)
        firstThreeInputs()
        sleep(0.15)
        naiveBot()
        shutil.rmtree('images')

    except KeyboardInterrupt:
        print("Ctrl-C pressed exiting..")
        shutil.rmtree('images')

if __name__ == "__main__":
    main()

