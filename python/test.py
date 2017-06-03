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

def main():
    cube = []
    failed = []
    passed = True
    for i in range(17):
        cube = get_cube_from_pictures(i)
        solution  = []
        make_cross(cube, solution)
        complete_first_layer(cube, solution)
        if test_first_layer(cube) == False:
            failed.append(i)
            passed = False
    if passed == True:
        print('all tests passed')
    else:
        print('some tests failed')
        for i in range(len(failed)):
            print_cube(cube)

main()
