def second_layer_algorithm_left(cube, solution):
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
    rotate = True
    sides = ["left", "bottom", "right"]
    things = {
        "o": ['g', 'r', 'b'],
        "g": ['r', 'b', 'o'],
        "r": ['b', 'o', 'g'],
        "b": ['o', 'g', 'r']
    }
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
