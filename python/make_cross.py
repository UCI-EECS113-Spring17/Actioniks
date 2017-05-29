import numpy as np

def check_front(cube, solution):
    frontColor = cube["front"][4]
    if cube["front"][1] == frontColor and cube["top"][7] != cube["top"][4]:
        rotate_up(cube, 2, solution)
        if cube["front"][3] == frontColor and cube["left"][5] != cube["left"][4]:
            rotate_left(cube, 2, solution)
            if cube["front"][5] == frontColor and cube["right"][3] != cube["right"][4]:
                rotate_right(cube, 2, solution)
                if (cube["front"][7] == frontColor and
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

def check_top(cube, solution):
    # normal = o > g > r > b
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
    print(solution)
