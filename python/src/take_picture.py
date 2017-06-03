from pynq import Overlay
from pynq.drivers.video import HDMI
from pynq.drivers.video import Frame
import cv2
import numpy as np
Overlay("base.bit").download()

def get_cube_from_pictures():
    return {
        "top": [
            'b', 'b', 'r',
            'g', 'o', 'w',
            'r', 'y', 'g'
        ],
        "left": [
            'r', 'o', 'g',
            'r', 'g', 'w',
            'b', 'b', 'w'
        ],
        "front": [
            'y', 'g', 'o',
            'g', 'w', 'o',
            'g', 'o', 'o'
        ],
        "right": [
            'y', 'b', 'w',
            'y', 'b', 'y',
            'y', 'r', 'o'
        ],
        "back": [
            'g', 'y', 'w',
            'r', 'y', 'w',
            'b', 'g', 'r'
        ],
        "bottom": [
            'o', 'w', 'b',
            'o', 'r', 'b',
            'y', 'r', 'w'
        ]
    }


def contains_color(filteredImage, colorChar):
    for y in range(3):
        for x in range(3):
            total = 0.0
            for i in range(y*int(frameHeight/3), (y+1)*int(frameHeight/3)):
                for j in range(x*int(frameWidth/3), (x+1)*int(frameWidth/3)):
                    total += filteredImage.item(i,j)
            if total/squareSize > 50:
                faceColors[y][x] = colorChar

def take_picture():
    cap = cv2.VideoCapture(0)
    _, uncropped = cap.read()
    frameWidth = 140
    frameHeight = 150
    squareSize = int(frameWidth * frameHeight / 9)
    # img[y: y + h, x: x + w]
    cubePicture = uncropped[240:240+frameHeight+1, 120:120+frameWidth+1]
    # cubePicture = uncropped

    hsv = cv2.cvtColor(cubePicture, cv2.COLOR_BGR2HSV)

    faceColors = [['0','0','0'],['0','0','0'],['0','0','0']]

    lowerBlue = np.array([110,100,50])
    upperBlue = np.array([130,255,255])
    blueSquares = cv2.inRange(hsv, lowerBlue, upperBlue)

    lowerYellow = np.array([20,100,100])
    upperYellow = np.array([40,255,255])
    yellowSquares = cv2.inRange(hsv, lowerYellow, upperYellow)

    lowerOrange = np.array([10,0,0])
    upperOrange = np.array([20,255,255])
    orangeSquares = cv2.inRange(hsv, lowerOrange, upperOrange)

    lowerGreen = np.array([50,100,100])
    upperGreen = np.array([70,255,255])
    greenSquares = cv2.inRange(hsv, lowerGreen, upperGreen)

    lowerWhite = np.array([0,0,100])
    upperWhite = np.array([255,100,255])
    whiteSquares = cv2.inRange(hsv, lowerWhite, upperWhite)

    lowerRed = np.array([0,0,100])
    upperRed = np.array([10,255,255])
    redSquares = cv2.inRange(hsv, lowerRed, upperRed)



    contains_color(blueSquares, 'b')
    contains_color(yellowSquares, 'y')
    contains_color(redSquares, 'r')
    contains_color(orangeSquares, 'o')
    contains_color(greenSquares, 'g')
    contains_color(whiteSquares, 'w')

    print(faceColors)

    %matplotlib inline
    from matplotlib import pyplot as plt
    plt.imshow(cubePicture)

    cap.release()

# take_picture()
