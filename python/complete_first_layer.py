
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
                print("moving")
                first_layer_algorithm(cube, solution)
        else:
            first_layer_algorithm(cube, solution)

def check_bottom_right_corner_back(cube, solution):
    flag = False
    print(cube["front"])
    print(cube["right"])
    print(cube["back"])
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
            flag = True
            while (cube["front"][8] != cube["front"][4] or
                    cube["right"][6] != cube["right"][4] or
                    cube["bottom"][2] != cube["bottom"][4]):
                first_layer_algorithm(cube, solution)
        else:
            print("skipping")
            first_layer_algorithm(cube, solution)
    return flag;

def complete_first_layer(cube, solution):
    # while (cube["front"][0] != cube["front"][4] or
    #         cube["front"][2] != cube["front"][4] or
    #         cube["front"][6] != cube["front"][4] or
    #         cube["front"][8] != cube["front"][4] or
    #         cube["bottom"][0] != cube["bottom"][4] or
    #         cube["bottom"][2] != cube["bottom"][4] or
    #         cube["top"][6] != cube["top"][4] or
    #         cube["top"][8] != cube["top"][4] or
    #         cube["right"][0] != cube["right"][4] or
    #         cube["right"][6] != cube["right"][4] or
    #         cube["left"][2] != cube["left"][4] or
    #         cube["left"][8] != cube["left"][4]):
    for i in range(20):
        # check_bottom_right_corner_front(cube, solution)
        print(i)
        check_bottom_right_corner_back(cube, solution)
        print(check_bottom_right_corner_back(cube, solution))
        rotate_cube_clockwise(cube, solution)

def main():
    cube = get_cube_from_pictures()
    solution  = []
    # print_cube(cube)
    make_cross(cube, solution)
    print()
    # print_cube(cube)
    # complete_first_layer(cube, solution)
    # print_cube(cube)
    # print("done")

main()
