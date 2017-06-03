def get_cube_from_pictures(i):
    if i == 0:
        return {
            "top": [
                'r', 'g', 'r',
                'b', 'o', 'o',
                'g', 'b', 'w',
            ],
            "left": [
                'b', 'r', 'o',
                'o', 'g', 'y',
                'y', 'w', 'w',
            ],
            "front": [
                'y', 'y', 'r',
                'r', 'w', 'w',
                'o', 'w', 'r',
            ],
            "right": [
                'b', 'w', 'w',
                'g', 'b', 'y',
                'y', 'y', 'o',
            ],
            "back": [
                'g', 'o', 'y',
                'g', 'y', 'b',
                'w', 'g', 'o',
            ],
            "bottom": [
                'b', 'r', 'g',
                'b', 'r', 'o',
                'b', 'r', 'g',
            ]
        }
    elif i == 1:
        return {
            "top": [
                'r', 'y', 'g',
                'w', 'o', 'w',
                'r', 'r', 'o',
            ],
            "left": [
                'g', 'g', 'y',
                'w', 'g', 'r',
                'o', 'o', 'w',
            ],
            "front": [
                'b', 'b', 'w',
                'y', 'w', 'b',
                'g', 'g', 'r',
            ],
            "right": [
                'b', 'o', 'y',
                'o', 'b', 'r',
                'w', 'g', 'y',
            ],
            "back": [
                'r', 'b', 'w',
                'w', 'y', 'b',
                'o', 'g', 'b',
            ],
            "bottom": [
                'o', 'o', 'b',
                'y', 'r', 'y',
                'y', 'r', 'g',
            ]
        }
    elif i == 2:
        return {
            "top": [
                'y', 'y', 'w',
                'w', 'o', 'y',
                'w', 'r', 'o',
            ],
            "left": [
                'g', 'g', 'o',
                'r', 'g', 'y',
                'y', 'g', 'y',
            ],
            "front": [
                'g', 'g', 'w',
                'g', 'w', 'o',
                'r', 'w', 'g',
            ],
            "right": [
                'b', 'o', 'r',
                'b', 'b', 'o',
                'y', 'y', 'g',
            ],
            "back": [
                'b', 'b', 'r',
                'w', 'y', 'b',
                'w', 'b', 'o',
            ],
            "bottom": [
                'b', 'r', 'o',
                'o', 'r', 'r',
                'b', 'w', 'r',
            ]
        }
    elif i == 3:
        return {
            "top": [
                'o', 'r', 'w',
                'b', 'o', 'g',
                'w', 'w', 'y',
            ],
            "left": [
                'y', 'w', 'b',
                'y', 'g', 'o',
                'w', 'o', 'o',
            ],
            "front": [
                'o', 'r', 'r',
                'y', 'w', 'y',
                'g', 'b', 'r',
            ],
            "right": [
                'g', 'y', 'g',
                'r', 'b', 'w',
                'b', 'g', 'g',
            ],
            "back": [
                'r', 'g', 'b',
                'o', 'y', 'b',
                'o', 'r', 'r',
            ],
            "bottom": [
                'y', 'o', 'y',
                'g', 'r', 'w',
                'b', 'b', 'w',
            ]
        }
    elif i == 4:
        return {
            "top": [
                'o', 'r', 'b',
                'y', 'o', 'o',
                'y', 'g', 'y',
            ],
            "left": [
                'w', 'o', 'b',
                'b', 'g', 'w',
                'w', 'b', 'r',
            ],
            "front": [
                'r', 'o', 'g',
                'g', 'w', 'b',
                'g', 'w', 'r',
            ],
            "right": [
                'o', 'b', 'y',
                'w', 'b', 'y',
                'y', 'o', 'b',
            ],
            "back": [
                'o', 'g', 'g',
                'g', 'y', 'r',
                'w', 'y', 'r',
            ],
            "bottom": [
                'w', 'r', 'g',
                'y', 'r', 'w',
                'b', 'r', 'o',
            ]
        }
    elif i == 5:
        return {
            "top": [
                'b', 'y', 'o',
                'y', 'o', 'b',
                'b', 'g', 'b',
            ],
            "left": [
                'o', 'b', 'o',
                'g', 'g', 'o',
                'w', 'r', 'w',
            ],
            "front": [
                'w', 'r', 'r',
                'w', 'w', 'w',
                'b', 'g', 'r',
            ],
            "right": [
                'y', 'o', 'g',
                'r', 'b', 'g',
                'y', 'y', 'g',
            ],
            "back": [
                'w', 'o', 'y',
                'y', 'y', 'o',
                'y', 'b', 'g',
            ],
            "bottom": [
                'r', 'w', 'g',
                'b', 'r', 'r',
                'r', 'w', 'o',
            ]
        }
    elif i == 6:
        return {
            "top": [
                'o', 'g', 'g',
                'w', 'o', 'g',
                'r', 'r', 'w',
            ],
            "left": [
                'b', 'r', 'y',
                'o', 'g', 'g',
                'g', 'o', 'y',
            ],
            "front": [
                'b', 'y', 'r',
                'w', 'w', 'y',
                'b', 'b', 'r',
            ],
            "right": [
                'b', 'o', 'o',
                'g', 'b', 'b',
                'g', 'r', 'r',
            ],
            "back": [
                'y', 'r', 'w',
                'o', 'y', 'w',
                'y', 'b', 'w',
            ],
            "bottom": [
                'o', 'w', 'w',
                'y', 'r', 'b',
                'o', 'y', 'g',
            ]
        }
    elif i == 7:
        return {
            "top": [
                'r', 'g', 'g',
                'o', 'o', 'w',
                'w', 'r', 'b',
            ],
            "left": [
                'w', 'w', 'o',
                'y', 'g', 'r',
                'o', 'y', 'r',
            ],
            "front": [
                'g', 'w', 'o',
                'b', 'w', 'o',
                'b', 'g', 'g',
            ],
            "right": [
                'w', 'b', 'o',
                'b', 'b', 'y',
                'r', 'o', 'r',
            ],
            "back": [
                'y', 'r', 'b',
                'r', 'y', 'b',
                'g', 'g', 'b',
            ],
            "bottom": [
                'y', 'w', 'y',
                'o', 'r', 'g',
                'y', 'y', 'w',
            ]
        }
    elif i == 8:
        return {
            "top": [
                'r', 'b', 'y',
                'y', 'o', 'w',
                'y', 'r', 'o',
            ],
            "left": [
                'g', 'o', 'g',
                'y', 'g', 'o',
                'b', 'g', 'o',
            ],
            "front": [
                'o', 'b', 'w',
                'b', 'w', 'w',
                'w', 'g', 'g',
            ],
            "right": [
                'b', 'o', 'o',
                'r', 'b', 'o',
                'r', 'y', 'b',
            ],
            "back": [
                'b', 'w', 'w',
                'g', 'y', 'b',
                'r', 'w', 'r',
            ],
            "bottom": [
                'g', 'r', 'y',
                'y', 'r', 'r',
                'y', 'g', 'w',
            ]
        }
    elif i == 9:
        return {
            "top": [
                'b', 'w', 'r',
                'w', 'o', 'g',
                'g', 'w', 'o',
            ],
            "left": [
                'r', 'r', 'y',
                'b', 'g', 'b',
                'b', 'g', 'b',
            ],
            "front": [
                'r', 'b', 'w',
                'y', 'w', 'o',
                'y', 'y', 'o',
            ],
            "right": [
                'b', 'r', 'w',
                'b', 'b', 'g',
                'w', 'w', 'g',
            ],
            "back": [
                'g', 'g', 'w',
                'o', 'y', 'r',
                'y', 'y', 'y',
            ],
            "bottom": [
                'r', 'r', 'g',
                'y', 'r', 'o',
                'o', 'o', 'o',
            ]
        }
    elif i == 10:
        return {
            "top": [
                'b', 'r', 'b',
                'y', 'o', 'o',
                'y', 'r', 'y',
            ],
            "left": [
                'y', 'o', 'g',
                'b', 'g', 'o',
                'o', 'g', 'b',
            ],
            "front": [
                'o', 'w', 'r',
                'b', 'w', 'w',
                'r', 'o', 'w',
            ],
            "right": [
                'g', 'w', 'o',
                'g', 'b', 'b',
                'r', 'r', 'b',
            ],
            "back": [
                'w', 'g', 'r',
                'w', 'y', 'y',
                'o', 'b', 'g',
            ],
            "bottom": [
                'w', 'g', 'g',
                'y', 'r', 'y',
                'w', 'r', 'y',
            ]
        }
    elif i == 11:
        return {
            "top": [
                'b', 'r', 'r',
                'y', 'o', 'w',
                'r', 'o', 'o',
            ],
            "left": [
                'w', 'r', 'b',
                'r', 'g', 'y',
                'y', 'o', 'w',
            ],
            "front": [
                'w', 'w', 'b',
                'g', 'w', 'b',
                'r', 'g', 'g',
            ],
            "right": [
                'y', 'b', 'y',
                'y', 'b', 'r',
                'o', 'g', 'y',
            ],
            "back": [
                'b', 'b', 'o',
                'g', 'y', 'w',
                'o', 'b', 'r',
            ],
            "bottom": [
                'g', 'o', 'w',
                'y', 'r', 'w',
                'g', 'o', 'g',
            ]
        }
    elif i == 12:
        return {
            "top": [
                'w', 'r', 'g',
                'b', 'o', 'y',
                'r', 'g', 'r',
            ],
            "left": [
                'g', 'o', 'b',
                'y', 'g', 'g',
                'b', 'y', 'g',
            ],
            "front": [
                'w', 'w', 'g',
                'o', 'w', 'b',
                'w', 'w', 'b',
            ],
            "right": [
                'y', 'g', 'o',
                'r', 'b', 'o',
                'y', 'r', 'w',
            ],
            "back": [
                'y', 'y', 'o',
                'w', 'y', 'o',
                'o', 'b', 'y',
            ],
            "bottom": [
                'r', 'r', 'r',
                'b', 'r', 'g',
                'o', 'w', 'b',
            ]
        }
    elif i == 13:
        return {
            "top": [
                'b', 'o', 'g',
                'y', 'o', 'y',
                'g', 'o', 'r',
            ],
            "left": [
                'o', 'b', 'w',
                'r', 'g', 'r',
                'o', 'o', 'r',
            ],
            "front": [
                'o', 'g', 'w',
                'g', 'w', 'o',
                'w', 'g', 'y',
            ],
            "right": [
                'g', 'g', 'y',
                'b', 'b', 'b',
                'r', 'y', 'o',
            ],
            "back": [
                'r', 'y', 'y',
                'w', 'y', 'b',
                'g', 'r', 'w',
            ],
            "bottom": [
                'b', 'w', 'b',
                'w', 'r', 'r',
                'b', 'w', 'y',
            ]
        }
    elif i == 14:
        return {
            "top": [
                'o', 'g', 'y',
                'g', 'o', 'b',
                'w', 'r', 'w',
            ],
            "left": [
                'w', 'o', 'g',
                'b', 'g', 'r',
                'b', 'r', 'g',
            ],
            "front": [
                'r', 'b', 'r',
                'w', 'w', 'w',
                'r', 'o', 'w',
            ],
            "right": [
                'b', 'w', 'b',
                'g', 'b', 'r',
                'o', 'w', 'o',
            ],
            "back": [
                'r', 'y', 'g',
                'y', 'y', 'y',
                'g', 'o', 'y',
            ],
            "bottom": [
                'y', 'y', 'b',
                'g', 'r', 'o',
                'o', 'b', 'y',
            ]
        }
    elif i == 15:
        return {
            "top": [
                'y', 'g', 'w',
                'w', 'o', 'b',
                'y', 'r', 'b',
            ],
            "left": [
                'g', 'r', 'o',
                'g', 'g', 'o',
                'b', 'r', 'y',
            ],
            "front": [
                'b', 'b', 'o',
                'b', 'w', 'o',
                'o', 'y', 'g',
            ],
            "right": [
                'w', 'w', 'o',
                'y', 'b', 'g',
                'w', 'w', 'y',
            ],
            "back": [
                'g', 'r', 'r',
                'w', 'y', 'o',
                'r', 'g', 'w',
            ],
            "bottom": [
                'g', 'b', 'r',
                'y', 'r', 'o',
                'r', 'y', 'b',
            ]
        }
    elif i == 16:
        return {
            "top": [
                'w', 'y', 'g',
                'b', 'o', 'g',
                'w', 'y', 'w',
            ],
            "left": [
                'r', 'r', 'b',
                'w', 'g', 'o',
                'y', 'g', 'b',
            ],
            "front": [
                'o', 'o', 'o',
                'w', 'w', 'y',
                'o', 'r', 'y',
            ],
            "right": [
                'g', 'r', 'y',
                'g', 'b', 'w',
                'o', 'g', 'w',
            ],
            "back": [
                'r', 'b', 'g',
                'r', 'y', 'b',
                'b', 'b', 'b',
            ],
            "bottom": [
                'y', 'y', 'g',
                'o', 'r', 'w',
                'r', 'o', 'r',
            ]
        }
    elif i == 17:
        return {
            "top": [
                'r', 'w', 'b',
                'g', 'o', 'o',
                'g', 'b', 'o',
            ],
            "left": [
                'g', 'y', 'y',
                'g', 'g', 'o',
                'o', 'o', 'o',
            ],
            "front": [
                'r', 'r', 'y',
                'y', 'w', 'r',
                'w', 'w', 'b',
            ],
            "right": [
                'g', 'b', 'r',
                'w', 'b', 'r',
                'r', 'r', 'o',
            ],
            "back": [
                'y', 'g', 'w',
                'y', 'y', 'o',
                'b', 'y', 'b',
            ],
            "bottom": [
                'g', 'b', 'w',
                'w', 'r', 'g',
                'y', 'b', 'w',
            ]
        }
    elif i == 18:
        return {
            "top": [
                'b', 'y', 'r',
                'o', 'o', 'w',
                'w', 'w', 'g',
            ],
            "left": [
                'w', 'y', 'g',
                'w', 'g', 'w',
                'b', 'r', 'g',
            ],
            "front": [
                'r', 'b', 'o',
                'r', 'w', 'o',
                'r', 'y', 'g',
            ],
            "right": [
                'y', 'o', 'b',
                'b', 'b', 'r',
                'o', 'o', 'b',
            ],
            "back": [
                'w', 'b', 'o',
                'g', 'y', 'g',
                'o', 'y', 'r',
            ],
            "bottom": [
                'y', 'g', 'w',
                'b', 'r', 'g',
                'y', 'r', 'y',
            ]
        }

    elif i == 19:
        return {
            "top": [
                'w', 'w', 'o',
                'g', 'o', 'y',
                'w', 'o', 'b',
            ],
            "left": [
                'b', 'r', 'g',
                'b', 'g', 'g',
                'g', 'b', 'o',
            ],
            "front": [
                'r', 'b', 'o',
                'o', 'w', 'w',
                'y', 'r', 'y',
            ],
            "right": [
                'w', 'o', 'g',
                'r', 'b', 'y',
                'g', 'o', 'y',
            ],
            "back": [
                'w', 'b', 'r',
                'g', 'y', 'y',
                'r', 'g', 'o',
            ],
            "bottom": [
                'b', 'y', 'r',
                'r', 'r', 'w',
                'y', 'w', 'b',
            ]
        }
