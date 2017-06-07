def main():
    cube = get_cube_from_pictures()
    solution = []
    print_cube(cube)
    make_cross(cube, solution)
    complete_first_layer(cube, solution)
    complete_second_layer(cube, solution)
    complete_third_layer(cube, solution)
    print_cube(cube)
    beautify(solution)
    print(solution)
    print_to_pmod_solution(solution)

main()
