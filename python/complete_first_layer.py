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
# if all(x >= 2 for x in (A, B, C, D)):
#     print A, B, C, D


def main():
    cube = get_cube_from_pictures()
    solution  = []
    make_cross(cube, solution)
    print_cube(cube)
    complete_first_layer(cube, solution)
    print_cube(cube)
    print(solution)

main()
