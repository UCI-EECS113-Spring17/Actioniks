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

        cube["bottom"][0] = cube["right"][0]
        cube["bottom"][1] = cube["right"][3]
        cube["bottom"][2] = cube["right"][6]

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
            solution.extend('B')

def rotate_cube_clockwise(cube, solution):
    rotate_back(cube, 3)
    rotate_front(cube)
    rotate_middle(cube)
    # solution.extend('C')
    solution.extend('BBBFM')
