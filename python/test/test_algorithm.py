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


def test_first_layer(cube):
    passed = True
    for i in range(9):
        if cube["front"][i] != cube["front"][4]:
            passed = False
            break
    if cube["top"][7] != cube["top"][4]:
        passed = False
    if cube["left"][5] != cube["left"][4]:
        passed = False
    if cube["right"][3] != cube["right"][4]:
        passed = False
    if cube["bottom"][1] != cube["bottom"][4]:
        passed = False
    return passed

def test_second_layer(cube):
    passed = True
    if cube["top"][3] != cube["top"][4]:
        passed = False
    if cube["top"][5] != cube["top"][4]:
        passed = False
    if cube["left"][1] != cube["left"][4]:
        passed = False
    if cube["left"][7] != cube["left"][4]:
        passed = False
    if cube["bottom"][3] != cube["bottom"][4]:
        passed = False
    if cube["bottom"][5] != cube["bottom"][4]:
        passed = False
    if cube["right"][1] != cube["right"][4]:
        passed = False
    if cube["right"][7] != cube["right"][4]:
        passed = False
    return passed

def test_final_layer(cube):
    sides = ["top", "bottom", "left", "right", "back", "front"]
    for i in range(6):
        for j in range(9):
            if cube[sides[i]][j] != cube[sides[i]][j]:
                return False
    return True

def remove_four_in_a_row(solution):
    for j in range(len(solution) - 3):
        temp = solution[j]
        if j + 4 > len(solution):
            break
        elif (solution[j + 1] == temp and
                solution[j + 2] == temp and
                solution[j + 3] == temp):
            del solution[j:j + 3]

def reverse_three_in_a_row(solution):
    for j in range(len(solution) - 2):
        temp = solution[j]
        if j + 3 > len(solution):
            break
        elif (solution[j + 1] == temp and
                solution[j + 2] == temp):
            del solution[j+1:j+2]
            solution[j] = temp + "'"

def main():
    cube = []
    failed = []
    passed = True
    totalMoves = 0
    for i in range(1):
        cube = get_cube_from_pictures(i)
        solution  = []
        make_cross(cube, solution)
        complete_first_layer(cube, solution)
        complete_second_layer(cube, solution)
        complete_third_layer(cube, solution)
        print_cube(cube)
        if test_final_layer(cube) == False:
            failed.append(i)
            passed = False
        else:
            remove_four_in_a_row(solution)
            reverse_three_in_a_row(solution)
            print(solution)
            totalMoves += len(solution)
    if passed == True:
        print('all tests passed')
    else:
        print('some tests failed\n')
        for i in range(len(failed)):
            print("number: " + str(failed[i]))
            print_cube(cube)
    print("total Moves: " + str(totalMoves))

main()
