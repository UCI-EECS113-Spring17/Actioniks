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
