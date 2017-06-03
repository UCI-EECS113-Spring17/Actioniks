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

def main():
    cube = []
    failed = []
    passed = True
    totalMoves = 0
    for i in range(20):
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
