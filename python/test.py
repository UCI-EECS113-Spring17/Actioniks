def test_cube_sides(cube, expected):
    x = 0
    mapThing = ["top", "left", "front", "right", "back", "bottom"]
    equal = True
    for i in range(len(cube)):
        for j in range(9):
            if cube[mapThing[i]][j] != expected[mapThing[i]][j]:
                equal = False
                print(mapThing[i] + " " + str(j) + " " + cube[mapThing[i]][j] +
                    " != " + expected[mapThing[i]][j])
    if equal:
        print("we did it fam")
    else:
        print("we didnt do it fam")

def expected_orientation_after_left_move():
    return {
        "top": [
            'r', 'b', 'r',
            'w', 'o', 'w',
            'w', 'y', 'g'
        ],
        "left": [
            'b', 'r', 'r',
            'b', 'g', 'o',
            'w', 'w', 'g'
        ],
        "front": [
            'b', 'g', 'o',
            'g', 'w', 'o',
            'r', 'o', 'o'
        ],
        "right": [
            'y', 'b', 'w',
            'y', 'b', 'y',
            'y', 'r', 'o'
        ],
        "back": [
            'g', 'y', 'y',
            'r', 'y', 'o',
            'b', 'g', 'o'
        ],
        "bottom": [
            'y', 'w', 'b',
            'g', 'r', 'b',
            'g', 'r', 'w'
        ]
    }

def expected_orientation_after_right_move():
    return {
        "top": [
            'b', 'b', 'o',
            'g', 'o', 'o',
            'r', 'y', 'o'
        ],
        "left": [
            'r', 'o', 'g',
            'r', 'g', 'w',
            'b', 'b', 'w'
        ],
        "front": [
            'y', 'g', 'b',
            'g', 'w', 'b',
            'g', 'o', 'w'
        ],
        "right": [
            'y', 'y', 'y',
            'r', 'b', 'b',
            'o', 'y', 'w'
        ],
        "back": [
            'g', 'y', 'w',
            'w', 'y', 'w',
            'r', 'g', 'r'
        ],
        "bottom": [
            'o', 'w', 'b',
            'o', 'r', 'r',
            'y', 'r', 'g'
        ]
    }

def expected_orientation_after_up_move():
    return {
        "top": [
            'r', 'g', 'b',
            'y', 'o', 'b',
            'g', 'w', 'r'
        ],
        "left": [
            'y', 'g', 'o',
            'r', 'g', 'w',
            'b', 'b', 'w'
        ],
        "front": [
            'y', 'b', 'w',
            'g', 'w', 'o',
            'g', 'o', 'o'
        ],
        "right": [
            'g', 'y', 'w',
            'y', 'b', 'y',
            'y', 'r', 'o'
        ],
        "back": [
            'r', 'o', 'g',
            'r', 'y', 'w',
            'b', 'g', 'r'
        ],
        "bottom": [
            'o', 'w', 'b',
            'o', 'r', 'b',
            'y', 'r', 'w'
        ]
    }



def expected_orientation_after_down_move():
    return {
        "top": [
            'b', 'b', 'r',
            'g', 'o', 'w',
            'r', 'y', 'g'
        ],
        "left": [
            'r', 'o', 'g',
            'r', 'g', 'w',
            'b', 'g', 'r'
        ],
        "front": [
            'y', 'g', 'o',
            'g', 'w', 'o',
            'b', 'b', 'w'
        ],
        "right": [
            'y', 'b', 'w',
            'y', 'b', 'y',
            'g', 'o', 'o'
        ],
        "back": [
            'g', 'y', 'w',
            'r', 'y', 'w',
            'y', 'r', 'o'
        ],
        "bottom": [
            'y', 'o', 'o',
            'r', 'r', 'w',
            'w', 'b', 'b'
        ]
    }


def expected_orientation_after_front_move():
    return {
        "top": [
            'b', 'b', 'r',
            'g', 'o', 'w',
            'w', 'w', 'g'
        ],
        "left": [
            'r', 'o', 'o',
            'r', 'g', 'w',
            'b', 'b', 'b'
        ],
        "front": [
            'g', 'g', 'y',
            'o', 'w', 'g',
            'o', 'o', 'o'
        ],
        "right": [
            'r', 'b', 'w',
            'y', 'b', 'y',
            'g', 'r', 'o'
        ],
        "back": [
            'g', 'y', 'w',
            'r', 'y', 'w',
            'b', 'g', 'r'
        ],
        "bottom": [
            'y', 'y', 'y',
            'o', 'r', 'b',
            'y', 'r', 'w'
        ]
    }


def expected_orientation_after_back_move():
    return {
        "top": [
            'w', 'y', 'o',
            'g', 'o', 'w',
            'r', 'y', 'g'
        ],
        "left": [
            'r', 'o', 'g',
            'b', 'g', 'w',
            'b', 'b', 'w'
        ],
        "front": [
            'y', 'g', 'o',
            'g', 'w', 'o',
            'g', 'o', 'o'
        ],
        "right": [
            'y', 'b', 'w',
            'y', 'b', 'r',
            'y', 'r', 'y'
        ],
        "back": [
            'b', 'r', 'g',
            'g', 'y', 'y',
            'r', 'w', 'w'
        ],
        "bottom": [
            'o', 'w', 'b',
            'o', 'r', 'b',
            'r', 'r', 'b'
        ]
    }

def expected_orientation_after_middle_move():
    return {
        "top": [
            'b', 'b', 'r',
            'b', 'g', 'o',
            'r', 'y', 'g'
        ],
        "left": [
            'r', 'o', 'g',
            'r', 'r', 'w',
            'b', 'b', 'w'
        ],
        "front": [
            'y', 'g', 'o',
            'g', 'w', 'o',
            'g', 'o', 'o'
        ],
        "right": [
            'y', 'g', 'w',
            'y', 'o', 'y',
            'y', 'w', 'o'
        ],
        "back": [
            'g', 'y', 'w',
            'r', 'y', 'w',
            'b', 'g', 'r'
        ],
        "bottom": [
            'o', 'w', 'b',
            'r', 'b', 'b',
            'y', 'r', 'w'
        ]
    }

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
