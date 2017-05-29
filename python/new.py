import numpy as np
import os
import cv2
from cv2 import *
import sys
import json

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

def expected_orientation_after_left_move():
    return {
        "top": [
            'r', 'b', 'r',
            'w', 'o', 'w',
            'w', 'y', 'g'
        ],
        "left": [
            'b', 'r', 'r',
            'b', 'g', 'o',
            'w', 'w', 'g'
        ],
        "front": [
            'b', 'g', 'o',
            'g', 'w', 'o',
            'r', 'o', 'o'
        ],
        "right": [
            'y', 'b', 'w',
            'y', 'b', 'y',
            'y', 'r', 'o'
        ],
        "back": [
            'g', 'y', 'y',
            'r', 'y', 'o',
            'b', 'g', 'o'
        ],
        "bottom": [
            'y', 'w', 'b',
            'g', 'r', 'b',
            'g', 'r', 'w'
        ]
    }

def rotate_left(cube):
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

def expected_orientation_after_right_move():
    return {
        "top": [
            'b', 'b', 'o',
            'g', 'o', 'o',
            'r', 'y', 'o'
        ],
        "left": [
            'r', 'o', 'g',
            'r', 'g', 'w',
            'b', 'b', 'w'
        ],
        "front": [
            'y', 'g', 'b',
            'g', 'w', 'b',
            'g', 'o', 'w'
        ],
        "right": [
            'y', 'y', 'y',
            'r', 'b', 'b',
            'o', 'y', 'w'
        ],
        "back": [
            'g', 'y', 'w',
            'w', 'y', 'w',
            'r', 'g', 'r'
        ],
        "bottom": [
            'o', 'w', 'b',
            'o', 'r', 'r',
            'y', 'r', 'g'
        ]
    }

def rotate_right(cube):
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


def rotate_up(cube):
    return 1;

def rotate_down(cube):
    return 1;

def rotate_front(cube):
    return 1;

def rotate_back(cube):
    return 1;

def test_cube_sides(cube, expected):
    x = 0
    mapThing = ["top", "left", "front", "right", "back", "bottom"]
    equal = True
    for i in range(len(cube)):
        for j in range(9):
            if cube[mapThing[i]][j] != expected[mapThing[i]][j]:
                equal = False
                print(mapThing[i] + " " + str(j) + " " + cube[mapThing[i]][j] +
                    " != " + expected[mapThing[i]][j])
    if equal:
        print("we did it fam")
    else:
        print("we didnt do it fam")

def cross(cube):
    # rotate_left(cube)
    # expected = expected_orientation_after_left_move()
    rotate_right(cube)
    expected = expected_orientation_after_right_move()
    test_cube_sides(cube, expected)

def main():
    cube = get_cube_from_pictures()
    cross(cube)

main()














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
