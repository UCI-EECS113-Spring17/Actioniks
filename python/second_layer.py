def get_cube_from_pictures():
    return {
        "top": [
            'o', 'b', 'y',
            'o', 'b', 'r',
            'b', 'b', 'b'
        ],
        "left": [
            'g', 'b', 'o',
            'y', 'o', 'o',
            'r', 'o', 'o'
        ],
        "front": [
            'w', 'w', 'w',
            'w', 'w', 'w',
            'w', 'w', 'w'
        ],
        "right": [
            'r', 'b', 'o',
            'r', 'r', 'y',
            'r', 'g', 'y'
        ],
        "back": [
            'b', 'y', 'y',
            'o', 'y', 'r',
            'r', 'g', 'g'
        ],
        "bottom": [
            'g', 'g', 'g',
            'g', 'g', 'r',
            'y', 'y', 'b'
        ]
    }

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
