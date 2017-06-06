from pynq import Overlay
from pynq.iop import Pmod_OLED
from pynq.iop import PMODA
from pynq.board import Button
import time
ol = Overlay('base.bit')
ol.download()
pmod_oled = Pmod_OLED(PMODA)
pmod_oled.clear()

def get_cube_from_pictures():
    i = 0
    j = False
    cube = {
        "top": [
            'X', 'X', 'X',
            'X', 'X', 'X',
            'X', 'X', 'X',
        ],
        "left": [
            'X', 'X', 'X',
            'X', 'X', 'X',
            'X', 'X', 'X',
        ],
        "front": [
            'X', 'X', 'X',
            'X', 'X', 'X',
            'X', 'X', 'X',
        ],
        "right": [
            'X', 'X', 'X',
            'X', 'X', 'X',
            'X', 'X', 'X',
        ],
        "back": [
            'X', 'X', 'X',
            'X', 'X', 'X',
            'X', 'X', 'X',
        ],
        "bottom": [
            'X', 'X', 'X',
            'X', 'X', 'X',
            'X', 'X', 'X',
        ]
    }

    def print_to_pmod_get_sides(i):
        pmod_oled.clear()
        remaining = 'Sides Remaining:' + str(6 - i)
        if i == 0:
            pmod_oled.write('Show Front,\n' + remaining)
        elif i == 1:
            pmod_oled.write('Show Top,\n' + remaining)
        elif i == 2:
            pmod_oled.write('Show Back,\n' + remaining)
        elif i == 3:
            pmod_oled.write('Show Bottom,\n' + remaining)
        elif i == 4:
            pmod_oled.write('Show Left,\n' + remaining)
        elif i == 5:
            pmod_oled.write('Show Right,\n' + remaining)

    print_to_pmod_get_sides(i)

    def draw_to_cube(i, listFromPic):
        print(listFromPic)
        order = ['front', 'top', 'back', 'bottom', 'left', 'right']
        if i == 2:
            for j in range(9):
                cube['back'][j] = listFromPic[8 - j]
        else:
            cube[order[i]] = listFromPic
        pmod_oled.clear()
        pmod_oled.write(
            listFromPic[0] + listFromPic[1] + listFromPic[2] + ' 0 if good\n' +
            listFromPic[3] + listFromPic[4] + listFromPic[5] + ' 1 if bad\n' +
            listFromPic[6] + listFromPic[7] + listFromPic[8])


    def process_input(i):
        pmod_oled.clear()
        pmod_oled.write('Taking Picture, please wait')
        draw_to_cube(i, get_side_from_picture())


    while i < 6:
        if Button(0).read():
            if j == True:
                print('called')
                i += 1
                print_to_pmod_get_sides(i)
                j = False
                time.sleep(1)
            else:
                print('other')
                process_input(i)
                j = True
        elif Button(1).read():
            if j == True:
                print_to_pmod_get_sides(i)
                j = False
                time.sleep(1)

    print(cube)
    pmod_oled.clear()
    pmod_oled.write('Calculating\nSolution...')
    return cube
