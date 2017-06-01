def get_cube_from_pictures():
    return {
        "top": [
            'b', 'y', 'r',
            'g', 'g', 'g',
            'g', 'g', 'g'
        ],
        "left": [
            'y', 'r', 'r',
            'y', 'r', 'r',
            'b', 'r', 'r'
        ],
        "front": [
            'w', 'w', 'w',
            'w', 'w', 'w',
            'w', 'w', 'w'
        ],
        "right": [
            'o', 'o', 'g',
            'o', 'o', 'y',
            'o', 'o', 'o'
        ],
        "back": [
            'y', 'b', 'r',
            'o', 'y', 'r',
            'g', 'g', 'y'
        ],
        "bottom": [
            'b', 'b', 'b',
            'b', 'b', 'b',
            'o', 'y', 'y'
        ]
    }

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

def complete_third_layer(cube, solution):
    # print_cube(cube)
    complete_back_cross(cube, solution)
    print()
    # print_cube(cube)
    match_back_edges_to_sides(cube, solution)
    print()
    print_cube(cube)
    position_back_corners_to_sides(cube, solution)
    print()
    print_cube(cube)

def main():
    cube = get_cube_from_pictures()
    solution  = []
    complete_third_layer(cube, solution)
    print()
    print(solution)

main()
