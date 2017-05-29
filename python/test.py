def get_cube_from_pictures():
    return {
        "top": [
            'b', 'b', 'r',
            'g', 'o', 'w',
            'r', 'y', 'g'
        ],
        "left": [
            'r', 'o', 'g',
            'r', 'g', 'w',
            'b', 'b', 'w'
        ],
        "front": [
            'y', 'g', 'o',
            'g', 'w', 'o',
            'g', 'o', 'o'
        ],
        "right": [
            'y', 'b', 'w',
            'y', 'b', 'y',
            'y', 'r', 'o'
        ],
        "back": [
            'g', 'y', 'w',
            'r', 'y', 'w',
            'b', 'g', 'r'
        ],
        "bottom": [
            'o', 'w', 'b',
            'o', 'r', 'b',
            'y', 'r', 'w'
        ]
    }

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
