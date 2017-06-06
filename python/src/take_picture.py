from pynq import Overlay
from pynq.drivers.video import HDMI
from pynq.drivers.video import Frame
import cv2
import numpy as np
Overlay('base.bit').download()

def get_side_from_picture():
    faceColors = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    faceColorAmounts = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    frameWidth = 190
    frameHeight = 190
    cap = cv2.VideoCapture(0)
    _, uncropped = cap.read()
    squareSize = int(frameWidth * frameHeight / 9)
    # img[y: y + h, x: x + w]
    cubePicture = uncropped[245:245+frameHeight, 195:195+frameWidth]
    # cubePicture = uncropped

    def contains_color(filteredImage, colorChar):
        for y in range(3):
            for x in range(3):
                total = 0.0
                for i in range(y * int(frameHeight / 3),
                        (y + 1) * int(frameHeight / 3)):
                    for j in range(x * int(frameWidth / 3),
                            (x + 1) * int(frameWidth / 3)):
                        total += filteredImage.item(i,j)
                if total/squareSize > faceColorAmounts[y * 3 + x]:
                    faceColors[y * 3 + x] = colorChar
                    faceColorAmounts[y * 3 + x] = total/squareSize

    hsv = cv2.cvtColor(cubePicture, cv2.COLOR_BGR2HSV)

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

    %matplotlib inline
    from matplotlib import pyplot as plt
    plt.imshow(cubePicture)

    cap.release()
    return faceColors
