def main():
    # cube = get_cube_from_pictures()
    cube = {
        "top": [
            'b', 'y', 'w',
            'y', 'o', 'y',
            'w', 'g', 'y',
        ],
        "left": [
            'o', 'r', 'r',
            'g', 'g', 'y',
            'w', 'o', 'o',
        ],
        "front": [
            'b', 'r', 'r',
            'o', 'w', 'r',
            'g', 'w', 'o',
        ],
        "right": [
            'g', 'b', 'o',
            'b', 'b', 'w',
            'b', 'b', 'b',
        ],
        "back": [
            'g', 'g', 'y',
            'g', 'y', 'o',
            'y', 'b', 'g',
        ],
        "bottom": [
            'y', 'r', 'w',
            'w', 'r', 'w',
            'r', 'o', 'r',
        ]
    }
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
