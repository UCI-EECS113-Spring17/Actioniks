from pynq import Overlay
Overlay('base.bit').download()
from pynq.drivers.video import HDMI
from pynq.drivers.video import Frame
from pynq.board import Button
from pynq.iop import Pmod_OLED
from pynq.iop import PMODA
import cv2
import numpy as np
import time
pmod_oled = Pmod_OLED(PMODA)
pmod_oled.clear()

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

def get_cube_from_pictures():
    i = 0
    j = False
    cube = {}

    def print_to_pmod_get_sides(i):
        pmod_oled.clear()
        remaining = 'Sides Remaining:' + str(6 - i)
        if i == 0:
            pmod_oled.write('Show Front,\n' + remaining)
        elif i == 1:
            pmod_oled.write('Show Top,\n' + remaining)
        elif i == 2:
            pmod_oled.write('Show Back,\n' + remaining)
        elif i == 3:
            pmod_oled.write('Show Bottom,\n' + remaining)
        elif i == 4:
            pmod_oled.write('Show Left,\n' + remaining)
        elif i == 5:
            pmod_oled.write('Show Right,\n' + remaining)

    print_to_pmod_get_sides(i)

    def draw_to_cube(i, listFromPic):
        print(listFromPic)
        order = ['front', 'top', 'back', 'bottom', 'left', 'right']
        cube[order[i]] = listFromPic
        pmod_oled.clear()
        pmod_oled.write(
            listFromPic[0] + listFromPic[1] + listFromPic[2] + ' 0 if good\n' +
            listFromPic[3] + listFromPic[4] + listFromPic[5] + ' 1 if bad\n' +
            listFromPic[6] + listFromPic[7] + listFromPic[8])


    def process_input(i):
        pmod_oled.clear()
        pmod_oled.write('Taking Picture, please wait')
        draw_to_cube(i, get_side_from_picture())


    while i < 6:
        if Button(0).read():
            if j == True:
                print('called')
                i += 1
                print_to_pmod_get_sides(i)
                j = False
                time.sleep(1)
            else:
                print('other')
                process_input(i)
                j = True
        elif Button(1).read():
            if j == True:
                print_to_pmod_get_sides(i)
                j = False
                time.sleep(1)

    print_cube(cube)
    pmod_oled.clear()
    pmod_oled.write('Calculating\nSolution...')
    return cube

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

def rotate_cube_clockwise(cube, solution, amount = 1):
    for i in range(amount):
        rotate_back(cube, 3)
        rotate_front(cube)
        rotate_middle(cube)
        solution.extend('C')
        # solution.extend('BBBFM')

def print_to_pmod_solution(solution):
    def convert_solution_index_to_pmod_output(move):
        if move == 'L':
            return 'Left'
        elif move == 'R':
            return 'Right'
        elif move == 'U':
            return 'Up'
        elif move == 'D':
            return 'Down'
        elif move == 'F':
            return 'Front'
        elif move == 'B':
            return 'Back'
        elif move == "L'":
            return 'Left Inverted'
        elif move == "R'":
            return 'Right Inverted'
        elif move == "U'":
            return 'Up Inverted'
        elif move == "D'":
            return 'Down Inverted'
        elif move == "F'":
            return 'Front Inverted'
        elif move == "B'":
            return 'Back Inverted'

    for i in range(len(solution)):
        pmod_oled.clear()
        pmod_oled.write(convert_solution_index_to_pmod_output(solution[i]))
        while True:
            if Button(0).read():
                break
    pmod_oled.clear()
    pmod_oled.write('Congratulations!  Your cube is solved')

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
                     rotate_cube_clockwise(cube, solution, i + 1)
                     top_determine_one(cube, solution)

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

def second_layer_algorithm_left(cube, solution):
    rotate_back(cube, 3, solution)
    rotate_left(cube, 3, solution)
    rotate_back(cube, 1, solution)
    rotate_left(cube, 1, solution)
    rotate_back(cube, 1, solution)
    rotate_up(cube, 1, solution)
    rotate_back(cube, 3, solution)
    rotate_up(cube, 3, solution)

def second_layer_algorithm_right(cube, solution):
    rotate_back(cube, 1, solution)
    rotate_right(cube, 1, solution)
    rotate_back(cube, 3, solution)
    rotate_right(cube, 3, solution)
    rotate_back(cube, 3, solution)
    rotate_up(cube, 3, solution)
    rotate_back(cube, 1, solution)
    rotate_up(cube, 1, solution)


def check_top_one_back_one(cube, solution):
    rotate = True
    sides = ["left", "bottom", "right"]
    if (cube["top"][1] == cube["top"][4] and
            cube["back"][1] == cube["left"][4]):
        second_layer_algorithm_left(cube, solution)
    elif (cube["top"][1] == cube["top"][4] and
            cube["back"][1] == cube["right"][4]):
        second_layer_algorithm_right(cube, solution)
    elif (cube["top"][3] == cube["left"][4] and
            cube["left"][1] == cube["top"][4]):
        second_layer_algorithm_left(cube, solution)
        rotate_back(cube, 2, solution)
        second_layer_algorithm_left(cube, solution)
    elif (cube["top"][5] == cube["right"][4] and
            cube["right"][1] == cube["top"][4]):
        second_layer_algorithm_right(cube, solution)
        rotate_back(cube, 2, solution)
        second_layer_algorithm_right(cube, solution)
    elif ((cube["top"][1] == cube["back"][4] or
            cube["back"][1] == cube["back"][4]) and
            (cube["left"][3] == cube["back"][4] or
            cube["back"][5] == cube["back"][4]) and
            (cube["bottom"][7] == cube["back"][4] or
            cube["back"][7] == cube["back"][4]) and
            (cube["right"][5] == cube["back"][4] or
            cube["back"][3] == cube["back"][4])):
        if cube["top"][3] != cube["top"][4]:
            second_layer_algorithm_left(cube, solution)
        elif cube["top"][5] != cube["top"][4]:
            second_layer_algorithm_right(cube, solution)
        else:
            rotate_cube_clockwise(cube, solution)
    else:
        for i in range(3):
            if (cube["top"][1] == cube[sides[i]][4] and
                    cube["back"][1] != cube["back"][4]):
                rotate = False
                rotate_back(cube, i + 1, solution)
                rotate_cube_clockwise(cube, solution, i + 1)
                top_determine_one(cube, solution)
        if rotate == True:
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

def third_layer_algorithm_cross(cube, solution):
    rotate_up(cube, 1, solution)
    rotate_right(cube, 1, solution)
    rotate_back(cube, 1, solution)
    rotate_right(cube, 3, solution)
    rotate_back(cube, 3, solution)
    rotate_up(cube, 3, solution)

def complete_back_cross(cube, solution):
    amountOfBack = 0
    for i in range(4):
        if cube["back"][i * 2 + 1] == cube["back"][4]:
            amountOfBack += 1
    if amountOfBack == 4:
        return
    elif amountOfBack == 0:
        third_layer_algorithm_cross(cube, solution)
    if (cube["back"][1] == cube["back"][4] and
            cube["back"][7] == cube["back"][4] and
            cube["back"][5] != cube["back"][4] and
            cube["back"][3] != cube["back"][4]):
        rotate_back(cube, 1, solution)
    if (cube["back"][3] == cube["back"][4] and
            cube["back"][5] == cube["back"][4] and
            cube["back"][1] != cube["back"][4] and
            cube["back"][7] != cube["back"][4]):
        third_layer_algorithm_cross(cube, solution)
        return

    while (cube["back"][5] != cube["back"][4] or
            cube["back"][7] != cube["back"][4]):
        rotate_cube_clockwise(cube, solution)
    third_layer_algorithm_cross(cube, solution)
    third_layer_algorithm_cross(cube, solution)

def third_layer_algorithm_swap_edges(cube, solution):
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
    while (check_back_edges_to_sides(cube, solution)):
        if cube["top"][1] == cube["top"][4]:
            rotate_cube_clockwise(cube, solution)
        elif (cube["top"][1] == cube["left"][4] and
                cube["left"][3] == cube["top"][4]):
            third_layer_algorithm_swap_edges(cube, solution)
        elif (cube["top"][1] == cube["bottom"][4] and
                cube["bottom"][7] == cube["top"][4]):
            third_layer_algorithm_swap_edges(cube, solution)
            rotate_cube_clockwise(cube, solution)
            rotate_cube_clockwise(cube, solution)
        else:
            rotate_back(cube, 1, solution)

def third_layer_algorithm_position_corners(cube, solution):
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
    rotate_right(cube, 3, solution)
    rotate_front(cube, 3, solution)
    rotate_right(cube, 1, solution)
    rotate_front(cube, 1, solution)

def finish_third_layer(cube, solution):
    for i in range(4):
        while (cube["top"][2] != cube["top"][1] or
                cube["right"][2] != cube["right"][5]):
            third_layer_final_algorithm(cube, solution)
        rotate_back(cube, 1, solution)

def complete_third_layer(cube, solution):
    complete_back_cross(cube, solution)
    match_back_edges_to_sides(cube, solution)
    position_back_corners_to_sides(cube, solution)
    finish_third_layer(cube, solution)

def main():
    print('starting')
    cube = get_cube_from_pictures()
    solution  = []
    make_cross(cube, solution)
    print_cube(cube)
    complete_first_layer(cube, solution)
    print_cube(cube)
    complete_second_layer(cube, solution)
    print_cube(cube)
    complete_third_layer(cube, solution)
    print_to_pmod(solution)
    print_cube(cube)
    print(solution)

main()
