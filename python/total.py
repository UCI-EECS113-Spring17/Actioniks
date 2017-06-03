from pynq import Overlay
from pynq.drivers.video import HDMI
from pynq.drivers.video import Frame
import cv2
import numpy as np
Overlay("base.bit").download()

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
# take_picture.py

def print_cube(cube):
    print("        " + cube["top"][0] + " " + cube["top"][1] + " " + cube["top"][2])
    print("        " + cube["top"][3] + " " + cube["top"][4] + " " + cube["top"][5])
    print("        " + cube["top"][6] + " " + cube["top"][7] + " " + cube["top"][8])
    print()
    print(
            cube["left"][0] + " " + cube["left"][1] + " " + cube["left"][2] + " | " +
            cube["front"][0] + " " + cube["front"][1] + " " + cube["front"][2] + " | " +
            cube["right"][0] + " " + cube["right"][1] + " " + cube["right"][2] + " | " +
            cube["back"][0] + " " + cube["back"][1] + " " + cube["back"][2]
    )
    print(
            cube["left"][3] + " " + cube["left"][4] + " " + cube["left"][5] + " | " +
            cube["front"][3] + " " + cube["front"][4] + " " + cube["front"][5] + " | " +
            cube["right"][3] + " " + cube["right"][4] + " " + cube["right"][5] + " | " +
            cube["back"][3] + " " + cube["back"][4] + " " + cube["back"][5]
    )
    print(
            cube["left"][6] + " " + cube["left"][7] + " " + cube["left"][8] + " | " +
            cube["front"][6] + " " + cube["front"][7] + " " + cube["front"][8] + " | " +
            cube["right"][6] + " " + cube["right"][7] + " " + cube["right"][8] + " | " +
            cube["back"][6] + " " + cube["back"][7] + " " + cube["back"][8]
    )
    print()
    print("        " + cube["bottom"][0] + " " + cube["bottom"][1] + " " + cube["bottom"][2])
    print("        " + cube["bottom"][3] + " " + cube["bottom"][4] + " " + cube["bottom"][5])
    print("        " + cube["bottom"][6] + " " + cube["bottom"][7] + " " + cube["bottom"][8])
    print()

#test.py

def rotate_side_counter_clockwise(side):
    temp = side[:]
    side[0] = temp[2]
    side[1] = temp[5]
    side[2] = temp[8]
    side[3] = temp[1]
    side[5] = temp[8]
    side[6] = temp[0]
    side[7] = temp[3]
    side[8] = temp[6]

def rotate_side_clockwise(side):
    temp = side[:]
    side[0] = temp[6]
    side[1] = temp[3]
    side[2] = temp[0]
    side[3] = temp[7]
    side[5] = temp[1]
    side[6] = temp[8]
    side[7] = temp[5]
    side[8] = temp[2]

def rotate_left(cube, amount = 1, solution = False):
    for i in range(amount):
        temp = cube["front"][:]
        rotate_side_clockwise(cube["left"])

        cube["front"][0] = cube["top"][0]
        cube["front"][3] = cube["top"][3]
        cube["front"][6] = cube["top"][6]

        cube["top"][0] = cube["back"][8]
        cube["top"][3] = cube["back"][5]
        cube["top"][6] = cube["back"][2]

        cube["back"][2] = cube["bottom"][6]
        cube["back"][5] = cube["bottom"][3]
        cube["back"][8] = cube["bottom"][0]

        cube["bottom"][0] = temp[0]
        cube["bottom"][3] = temp[3]
        cube["bottom"][6] = temp[6]
        if solution != False:
            solution.extend('L')

def rotate_right(cube, amount = 1, solution = False):
    for i in range(amount):
        temp = cube["back"][:]
        rotate_side_clockwise(cube["right"])

        cube["back"][0] = cube["top"][8]
        cube["back"][3] = cube["top"][5]
        cube["back"][6] = cube["top"][2]

        cube["top"][2] = cube["front"][2]
        cube["top"][5] = cube["front"][5]
        cube["top"][8] = cube["front"][8]

        cube["front"][2] = cube["bottom"][2]
        cube["front"][5] = cube["bottom"][5]
        cube["front"][8] = cube["bottom"][8]

        cube["bottom"][2] = temp[6]
        cube["bottom"][5] = temp[3]
        cube["bottom"][8] = temp[0]
        if solution != False:
            solution.extend('R')

def rotate_up(cube, amount = 1, solution = False):
    for i in range(amount):
        temp = cube["front"][:]
        rotate_side_clockwise(cube["top"])

        cube["front"][0] = cube["right"][0]
        cube["front"][1] = cube["right"][1]
        cube["front"][2] = cube["right"][2]

        cube["right"][0] = cube["back"][0]
        cube["right"][1] = cube["back"][1]
        cube["right"][2] = cube["back"][2]

        cube["back"][0] = cube["left"][0]
        cube["back"][1] = cube["left"][1]
        cube["back"][2] = cube["left"][2]

        cube["left"][0] = temp[0]
        cube["left"][1] = temp[1]
        cube["left"][2] = temp[2]
        if solution != False:
            solution.extend('U')


def rotate_down(cube, amount = 1, solution = False):
    for i in range(amount):
        temp = cube["back"][:]
        rotate_side_clockwise(cube["bottom"])

        cube["back"][6] = cube["right"][6]
        cube["back"][7] = cube["right"][7]
        cube["back"][8] = cube["right"][8]

        cube["right"][6] = cube["front"][6]
        cube["right"][7] = cube["front"][7]
        cube["right"][8] = cube["front"][8]

        cube["front"][6] = cube["left"][6]
        cube["front"][7] = cube["left"][7]
        cube["front"][8] = cube["left"][8]

        cube["left"][6] = temp[6]
        cube["left"][7] = temp[7]
        cube["left"][8] = temp[8]
        if solution != False:
            solution.extend('D')

def rotate_front(cube, amount = 1, solution = False):
    for i in range(amount):
        temp = cube["bottom"][:]
        rotate_side_clockwise(cube["front"])

        cube["bottom"][2] = cube["right"][0]
        cube["bottom"][1] = cube["right"][3]
        cube["bottom"][0] = cube["right"][6]

        cube["right"][0] = cube["top"][6]
        cube["right"][3] = cube["top"][7]
        cube["right"][6] = cube["top"][8]

        cube["top"][6] = cube["left"][8]
        cube["top"][7] = cube["left"][5]
        cube["top"][8] = cube["left"][2]

        cube["left"][2] = temp[0]
        cube["left"][5] = temp[1]
        cube["left"][8] = temp[2]
        if solution != False:
            solution.extend('F')

def rotate_back(cube, amount = 1, solution = False):
    for i in range(amount):
        temp = cube["top"][:]
        rotate_side_clockwise(cube["back"])

        cube["top"][0] = cube["right"][2]
        cube["top"][1] = cube["right"][5]
        cube["top"][2] = cube["right"][8]

        cube["right"][2] = cube["bottom"][8]
        cube["right"][5] = cube["bottom"][7]
        cube["right"][8] = cube["bottom"][6]

        cube["bottom"][6] = cube["left"][0]
        cube["bottom"][7] = cube["left"][3]
        cube["bottom"][8] = cube["left"][6]

        cube["left"][0] = temp[2]
        cube["left"][3] = temp[1]
        cube["left"][6] = temp[0]
        if solution != False:
            solution.extend('B')

def rotate_middle(cube, amount = 1, solution = False):
    for i in range(amount):
        temp = cube["top"][:]
        cube["top"][3] = cube["left"][7]
        cube["top"][4] = cube["left"][4]
        cube["top"][5] = cube["left"][1]

        cube["left"][1] = cube["bottom"][3]
        cube["left"][4] = cube["bottom"][4]
        cube["left"][7] = cube["bottom"][5]

        cube["bottom"][5] = cube["right"][1]
        cube["bottom"][4] = cube["right"][4]
        cube["bottom"][3] = cube["right"][7]

        cube["right"][1] = temp[3]
        cube["right"][4] = temp[4]
        cube["right"][7] = temp[5]
        if solution != False:
            solution.extend('M')

def rotate_cube_clockwise(cube, solution):
    rotate_back(cube, 3)
    rotate_front(cube)
    rotate_middle(cube)
    # solution.extend('C')
    solution.extend('BBBFM')

# rotate_cube.py

def check_front(cube, solution):
    if (cube["front"][1] == cube["front"][4] and
            cube["top"][7] != cube["top"][4]):
        rotate_up(cube, 2, solution)
    if (cube["front"][3] == cube["front"][4] and
            cube["left"][5] != cube["left"][4]):
        rotate_left(cube, 2, solution)
    if (cube["front"][5] == cube["front"][4] and
            cube["right"][3] != cube["right"][4]):
        rotate_right(cube, 2, solution)
    if (cube["front"][7] == cube["front"][4] and
            cube["bottom"][1] != cube["bottom"][4]):
        rotate_down(cube, 2, solution)

def check_back(cube, solution):
    things = {
        "o": ['g', 'r', 'b'],
        "g": ['r', 'b', 'o'],
        "r": ['b', 'o', 'g'],
        "b": ['o', 'g', 'r']
    }
    if cube["back"][1] == cube["front"][4]:
        if cube["top"][1] == cube["top"][4]:
            rotate_up(cube, 2, solution)
        elif cube["top"][1] == things[cube["top"][4]][0]:
            rotate_back(cube, 1, solution)
            rotate_left(cube, 2, solution)
        elif cube["top"][1] == things[cube["top"][4]][1]:
            rotate_back(cube, 2, solution)
            rotate_down(cube, 2, solution)
        elif cube["top"][1] == things[cube["top"][4]][2]:
            rotate_back(cube, 3, solution)
            rotate_right(cube, 2, solution)

    if cube["back"][3] == cube["front"][4]:
        if cube["right"][5] == cube["right"][4]:
            rotate_right(cube, 2, solution)
        elif cube["right"][5] == things[cube["right"][4]][0]:
            rotate_back(cube, 1, solution)
            rotate_up(cube, 2, solution)
        elif cube["right"][5] == things[cube["right"][4]][1]:
            rotate_back(cube, 2, solution)
            rotate_left(cube, 2, solution)
        elif cube["right"][5] == things[cube["right"][4]][2]:
            rotate_back(cube, 3, solution)
            rotate_down(cube, 2, solution)

    if cube["back"][5] == cube["front"][4]:
        if cube["left"][3] == cube["left"][4]:
            rotate_left(cube, 2, solution)
        elif cube["left"][3] == things[cube["left"][4]][0]:
            rotate_back(cube, 1, solution)
            rotate_down(cube, 2, solution)
        elif cube["left"][3] == things[cube["left"][4]][1]:
            rotate_back(cube, 2, solution)
            rotate_right(cube, 2, solution)
        elif cube["left"][3] == things[cube["left"][4]][2]:
            rotate_back(cube, 3, solution)
            rotate_up(cube, 2, solution)

    if cube["back"][7] == cube["front"][4]:
        if cube["bottom"][7] == cube["bottom"][4]:
            rotate_down(cube, 2, solution)
        elif cube["bottom"][7] == things[cube["bottom"][4]][0]:
            rotate_back(cube, 1, solution)
            rotate_right(cube, 2, solution)
        elif cube["bottom"][7] == things[cube["bottom"][4]][1]:
            rotate_back(cube, 2, solution)
            rotate_up(cube, 2, solution)
        elif cube["bottom"][7] == things[cube["bottom"][4]][2]:
            rotate_back(cube, 3, solution)
            rotate_left(cube, 2, solution)

def top_determine_one(cube, solution):
     things = {
         "o": ['g', 'r', 'b'],
         "g": ['r', 'b', 'o'],
         "r": ['b', 'o', 'g'],
         "b": ['o', 'g', 'r']
     }
     if cube["top"][1] == cube["front"][4]:
         if cube["back"][1] == cube["top"][4]:
            rotate_up(cube, 3, solution)
            rotate_left(cube, 1, solution)
            rotate_front(cube, 1, solution)
            rotate_up(cube, 1, solution)
            rotate_front(cube, 3, solution)
            rotate_up(cube, 3, solution)
         else:
             for i in range(3):
                 if cube["back"][1] == things[cube["top"][4]][i]:
                     rotate_back(cube, i + 1, solution)

def check_top(cube, solution):
    top_determine_one(cube, solution)

    if cube["top"][3] == cube["front"][4]:
        if cube["left"][1] == cube["left"][4]:
            rotate_left(cube, 1, solution)
        else:
            rotate_up(cube, 1, solution)
            top_determine_one(cube, solution)
            rotate_up(cube, 3, solution)

    if cube["top"][5] == cube["front"][4]:
        if cube["right"][1] == cube["right"][4]:
            rotate_right(cube, 3, solution)
        else:
            rotate_up(cube, 3, solution)
            top_determine_one(cube, solution)
            rotate_up(cube, 1, solution)

    if cube["top"][7] == cube["front"][4]:
        rotate_up(cube, 2, solution)
        top_determine_one(cube, solution)
        rotate_up(cube, 2, solution)

def make_cross(cube, solution):
    while (cube["front"][1] != cube["front"][4] or
            cube["front"][3] != cube["front"][4] or
            cube["front"][5] != cube["front"][4] or
            cube["front"][7] != cube["front"][4] or
            cube["bottom"][1] != cube["bottom"][4] or
            cube["right"][3] != cube["right"][4] or
            cube["left"][5] != cube["left"][4] or
            cube["top"][7] != cube["top"][4]):
        check_front(cube, solution)
        check_back(cube, solution)
        check_top(cube, solution)
        rotate_cube_clockwise(cube, solution)

# make_cross.py

def first_layer_algorithm(cube, solution):
    rotate_right(cube, 3, solution)
    rotate_back(cube, 3, solution)
    rotate_right(cube, 1, solution)
    rotate_back(cube, 1, solution)

def check_bottom_right_corner_front(cube, solution):
    if (cube["front"][8] == cube["front"][4] or
            cube["right"][6] == cube["front"][4] or
            cube["bottom"][2] == cube["front"][4]):
        if (cube["front"][8] == cube["front"][4] or
                cube["front"][8] == cube["bottom"][4] or
                cube["front"][8] == cube["right"][4]
                ) and (
                cube["right"][6] == cube["front"][4] or
                cube["right"][6] == cube["bottom"][4] or
                cube["right"][6] == cube["right"][4]
                ) and (
                cube["bottom"][2] == cube["front"][4] or
                cube["bottom"][2] == cube["bottom"][4] or
                cube["bottom"][2] == cube["right"][4]):
            while (cube["front"][8] != cube["front"][4] or
                    cube["right"][6] != cube["right"][4] or
                    cube["bottom"][2] != cube["bottom"][4]):
                first_layer_algorithm(cube, solution)
        else:
            first_layer_algorithm(cube, solution)

def check_bottom_right_corner_back(cube, solution):
    corner = [cube["right"][8], cube["back"][6], cube["bottom"][8]]
    if (cube["right"][8] == cube["front"][4] or
            cube["back"][6] == cube["front"][4] or
            cube["bottom"][8] == cube["front"][4]):
        if (cube["right"][8] == cube["front"][4] or
                cube["right"][8] == cube["bottom"][4] or
                cube["right"][8] == cube["right"][4]
                ) and (
                cube["back"][6] == cube["front"][4] or
                cube["back"][6] == cube["bottom"][4] or
                cube["back"][6] == cube["right"][4]
                ) and (
                cube["bottom"][8] == cube["front"][4] or
                cube["bottom"][8] == cube["bottom"][4] or
                cube["bottom"][8] == cube["right"][4]):
            while (cube["front"][8] != cube["front"][4] or
                    cube["right"][6] != cube["right"][4] or
                    cube["bottom"][2] != cube["bottom"][4]):
                first_layer_algorithm(cube, solution)
        else:
            if 'o' in corner and 'b' in corner:
                if cube["top"][4] == 'o':
                    rotate_back(cube, 1, solution)
                elif cube["top"][4] == 'b':
                    rotate_back(cube, 2, solution)
                elif cube["top"][4] == 'r':
                    rotate_back(cube, 3, solution)
            elif 'o' in corner and 'g' in corner:
                if cube["top"][4] == 'g':
                    rotate_back(cube, 1, solution)
                elif cube["top"][4] == 'o':
                    rotate_back(cube, 2, solution)
                elif cube["top"][4] == 'b':
                    rotate_back(cube, 3, solution)
            elif 'r' in corner and 'b' in corner:
                if cube["top"][4] == 'b':
                    rotate_back(cube, 1, solution)
                elif cube["top"][4] == 'r':
                    rotate_back(cube, 2, solution)
                elif cube["top"][4] == 'g':
                    rotate_back(cube, 3, solution)
            elif 'r' in corner and 'g' in corner:
                if cube["top"][4] == 'r':
                    rotate_back(cube, 1, solution)
                elif cube["top"][4] == 'g':
                    rotate_back(cube, 2, solution)
                elif cube["top"][4] == 'o':
                    rotate_back(cube, 3, solution)

def complete_first_layer(cube, solution):
    while (cube["front"][0] != cube["front"][4] or
            cube["front"][2] != cube["front"][4] or
            cube["front"][6] != cube["front"][4] or
            cube["front"][8] != cube["front"][4] or
            cube["bottom"][0] != cube["bottom"][4] or
            cube["bottom"][2] != cube["bottom"][4] or
            cube["top"][6] != cube["top"][4] or
            cube["top"][8] != cube["top"][4] or
            cube["right"][0] != cube["right"][4] or
            cube["right"][6] != cube["right"][4] or
            cube["left"][2] != cube["left"][4] or
            cube["left"][8] != cube["left"][4]):
        check_bottom_right_corner_front(cube, solution)
        check_bottom_right_corner_back(cube, solution)
        rotate_cube_clockwise(cube, solution)

# complete_first_layer.py

def second_layer_algorithm_left(cube, solution):
    print("left")
    # U'  L'  U L U F U'  F'
    # BBB LLL B L B U BBB UUU
    rotate_back(cube, 3, solution)
    rotate_left(cube, 3, solution)
    rotate_back(cube, 1, solution)
    rotate_left(cube, 1, solution)
    rotate_back(cube, 1, solution)
    rotate_up(cube, 1, solution)
    rotate_back(cube, 3, solution)
    rotate_up(cube, 3, solution)

def second_layer_algorithm_right(cube, solution):
    print("right")
    # U R U'  R'  U'  F'  U F
    # B R BBB RRR BBB UUU B U
    rotate_back(cube, 1, solution)
    rotate_right(cube, 1, solution)
    rotate_back(cube, 3, solution)
    rotate_right(cube, 3, solution)
    rotate_back(cube, 3, solution)
    rotate_up(cube, 3, solution)
    rotate_back(cube, 1, solution)
    rotate_up(cube, 1, solution)


def check_top_one_back_one(cube, solution):
    if (cube["back"][1] != cube["back"][4]):
        if cube["top"][1] == cube["top"][4]:
            if cube["back"][1] == cube["right"][4]:
                second_layer_algorithm_right(cube, solution)
            elif cube["back"][1] == cube["left"][4]:
                second_layer_algorithm_left(cube, solution)
        elif cube["top"][1] == cube["left"][4]:
            rotate_cube_clockwise(cube, solution)
        elif cube["top"][1] == cube["bottom"][4]:
            rotate_cube_clockwise(cube, solution)
            rotate_cube_clockwise(cube, solution)
        elif cube["top"][1] == cube["right"][4]:
            rotate_cube_clockwise(cube, solution)
            rotate_cube_clockwise(cube, solution)
            rotate_cube_clockwise(cube, solution)
    if (cube["left"][3] == cube["left"][4] and
            cube["back"][5] != cube["back"][4]):
        rotate_cube_clockwise(cube, solution)
    elif (cube["bottom"][7] == cube["bottom"][4] and
            cube["back"][7] != cube["back"][4]):
        rotate_cube_clockwise(cube, solution)
        rotate_cube_clockwise(cube, solution)
    elif (cube["right"][5] == cube["right"][4] and
            cube["back"][3] != cube["back"][4]):
        rotate_cube_clockwise(cube, solution)
        rotate_cube_clockwise(cube, solution)
        rotate_cube_clockwise(cube, solution)
    else:
        if (cube["top"][5] == cube["right"][4] and
                cube["right"][1] == cube["top"][4]):
            second_layer_algorithm_right(cube, solution)
            rotate_back(cube, 2, solution)
            second_layer_algorithm_right(cube, solution)
        elif (cube["top"][3] == cube["left"][4] and
                cube["left"][1] == cube["top"][4]):
            second_layer_algorithm_left(cube, solution)
            rotate_back(cube, 2, solution)
            second_layer_algorithm_left(cube, solution)
        else:
            rotate_cube_clockwise(cube, solution)

def complete_second_layer(cube, solution):
    while (cube["top"][3] != cube["top"][4] or
            cube["top"][5] != cube["top"][4] or
            cube["left"][1] != cube["left"][4] or
            cube["left"][7] != cube["left"][4] or
            cube["right"][1] != cube["right"][4] or
            cube["right"][7] != cube["right"][4] or
            cube["bottom"][3] != cube["bottom"][4] or
            cube["bottom"][5] != cube["bottom"][4]):
        check_top_one_back_one(cube, solution)

# complete_second_layer.py

def third_layer_algorithm_cross(cube, solution):
    # F R U R'  U'  F'
    # U R B RRR BBB UUU
    rotate_up(cube, 1, solution)
    rotate_right(cube, 1, solution)
    rotate_back(cube, 1, solution)
    rotate_right(cube, 3, solution)
    rotate_back(cube, 3, solution)
    rotate_up(cube, 3, solution)

def complete_back_cross(cube, solution):
    if cube["back"][1] != cube["back"][4]:
        third_layer_algorithm_cross(cube, solution)
        while (cube["back"][5] != cube["back"][4] or
                cube["back"][7] != cube["back"][4]):
            rotate_cube_clockwise(cube, solution)
        third_layer_algorithm_cross(cube, solution)
        third_layer_algorithm_cross(cube, solution)
    elif cube["back"][7] != cube["back"][4]:
        third_layer_algorithm_cross(cube, solution)
        third_layer_algorithm_cross(cube, solution)
    elif (cube["back"][3] != cube["back"][4] or
            cube["back"][5] != cube["back"][4]):
        third_layer_algorithm_cross(cube, solution)


def third_layer_algorithm_swap_edges(cube, solution):
    # R U R'  U R U2 R'  U
    # R B RRR B R BB RRR B
    rotate_right(cube, 1, solution)
    rotate_back(cube, 1, solution)
    rotate_right(cube, 3, solution)
    rotate_back(cube, 1, solution)
    rotate_right(cube, 1, solution)
    rotate_back(cube, 2, solution)
    rotate_right(cube, 3, solution)
    rotate_back(cube, 1, solution)

def check_back_edges_to_sides(cube, solution):
    if (cube["top"][1] != cube["top"][4] or
            cube["right"][5] != cube["right"][4] or
            cube["bottom"][7] != cube["bottom"][4] or
            cube["left"][3] != cube["left"][4]):
        return True;
    else:
        return False;

def match_back_edges_to_sides(cube, solution):
    sideOrder = {
        'o': 'b',
        'b': 'r',
        'r': 'g',
        'g': 'o'
    }
    realOrder = [
        cube["top"][1],
        cube["right"][5],
        cube["bottom"][7],
        cube["left"][3],
        cube["top"][1]
    ]
    while (check_back_edges_to_sides(cube, solution)):
        for i in range(4):
            if sideOrder[realOrder[i]] == realOrder[i + 1]:
                while cube["top"][4] != realOrder[i + 1]:
                    rotate_cube_clockwise(cube, solution)
                while cube["bottom"][7] != cube["bottom"][4]:
                    rotate_back(cube, 1, solution)
                break
        if(check_back_edges_to_sides(cube, solution)):
            third_layer_algorithm_swap_edges(cube, solution)

def third_layer_algorithm_position_corners(cube, solution):
    # U R U'  L'  U R'  U'  L
    # B R BBB LLL B RRR BBB L
    rotate_back(cube, 1, solution)
    rotate_right(cube, 1, solution)
    rotate_back(cube, 3, solution)
    rotate_left(cube, 3, solution)
    rotate_back(cube, 1, solution)
    rotate_right(cube, 3, solution)
    rotate_back(cube, 3, solution)
    rotate_left(cube, 1, solution)

def position_back_corners_to_sides(cube, solution):
    i = 0
    while ( # top right
            (
            cube["top"][2] != cube["top"][4] and
            cube["top"][2] != cube["back"][4] and
            cube["top"][2] != cube["right"][4]
            ) or
            (
            cube["right"][2] != cube["top"][4] and
            cube["right"][2] != cube["back"][4] and
            cube["right"][2] != cube["right"][4]
            ) or
            (
            cube["back"][0] != cube["top"][4] and
            cube["back"][0] != cube["back"][4] and
            cube["back"][0] != cube["right"][4]
            ) or
            # top left
            (
            cube["top"][0] != cube["top"][4] and
            cube["top"][0] != cube["back"][4] and
            cube["top"][0] != cube["left"][4]
            ) or
            (
            cube["left"][0] != cube["top"][4] and
            cube["left"][0] != cube["back"][4] and
            cube["left"][0] != cube["left"][4]
            ) or
            (
            cube["back"][2] != cube["top"][4] and
            cube["back"][2] != cube["back"][4] and
            cube["back"][2] != cube["left"][4]
            ) or
            # bottom right
            (
            cube["bottom"][8] != cube["bottom"][4] and
            cube["bottom"][8] != cube["back"][4] and
            cube["bottom"][8] != cube["right"][4]
            ) or
            (
            cube["right"][8] != cube["bottom"][4] and
            cube["right"][8] != cube["back"][4] and
            cube["right"][8] != cube["right"][4]
            ) or
            (
            cube["back"][6] != cube["bottom"][4] and
            cube["back"][6] != cube["back"][4] and
            cube["back"][6] != cube["right"][4]
            ) or
            # bottom left
            (
            cube["bottom"][6] != cube["bottom"][4] and
            cube["bottom"][6] != cube["back"][4] and
            cube["bottom"][6] != cube["left"][4]
            ) or
            (
            cube["left"][6] != cube["bottom"][4] and
            cube["left"][6] != cube["back"][4] and
            cube["left"][6] != cube["left"][4]
            ) or
            (
            cube["back"][8] != cube["bottom"][4] and
            cube["back"][8] != cube["back"][4] and
            cube["back"][8] != cube["left"][4]
            )):
        if ((cube["top"][2] != cube["top"][4] and
                cube["top"][2] != cube["back"][4] and
                cube["top"][2] != cube["right"][4]) or
                (cube["right"][2] != cube["top"][4] and
                cube["right"][2] != cube["back"][4] and
                cube["right"][2] != cube["right"][4]) or
                (cube["back"][0] != cube["top"][4] and
                cube["back"][0] != cube["back"][4] and
                cube["back"][0] != cube["right"][4])):
            rotate_cube_clockwise(cube, solution)
            i += 1
        else:
            third_layer_algorithm_position_corners(cube, solution)
            i = 0
        if i  == 4:
            i = 0
            third_layer_algorithm_position_corners(cube, solution)

def third_layer_final_algorithm(cube, solution):
    # R'  D'  R D
    # RRR FFF R F
    rotate_right(cube, 3, solution)
    rotate_front(cube, 3, solution)
    rotate_right(cube, 1, solution)
    rotate_front(cube, 1, solution)

def finish_third_layer(cube, solution):
    for i in range(4):
        while (cube["top"][2] != cube["top"][1] and
                cube["right"][2] != cube["right"][5]):
            third_layer_final_algorithm(cube, solution)
            print(i)
        rotate_back(cube, 1, solution)

def complete_third_layer(cube, solution):
    complete_back_cross(cube, solution)
    match_back_edges_to_sides(cube, solution)
    position_back_corners_to_sides(cube, solution)
    finish_third_layer(cube, solution)

# complete_third_layer.py

# def main():
#     cube = get_cube_from_pictures()
#     solution  = []
#     make_cross(cube, solution)
#     print_cube(cube)
#     complete_first_layer(cube, solution)
#     print_cube(cube)
#     complete_second_layer(cube, solution)
#     print_cube(cube)
#     complete_third_layer(cube, solution)
#     print_cube(cube)
#     print(solution)
#
# main()

# main.py
