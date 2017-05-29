def main():
    cube = get_cube_from_pictures()
    solution  = []
    make_cross(cube, solution)
    complete_first_layer(cube, solution)

main()
