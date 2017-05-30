def main():
    cube = get_cube_from_pictures()
    solution  = []
    make_cross(cube, solution)
    print_cube(cube)
    complete_first_layer(cube, solution)
    print_cube(cube)
    print(solution)

main()
