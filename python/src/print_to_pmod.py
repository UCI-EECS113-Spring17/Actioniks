from pynq import Overlay
from pynq.iop import Pmod_OLED
from pynq.iop import PMODA
from pynq.board import Button
import time
ol = Overlay("base.bit")
ol.download()
pmod_oled = Pmod_OLED(PMODA)

def print_to_pmod_solution(solution):
    for i in range(len(solution)):
        pmod_oled.clear()
        pmod_oled.write(solution[i])
        while True:
            if Button(0).read():
                time.sleep(1)
                break
    pmod_oled.clear()
    pmod_oled.write('Congratulations!\nYour cube is\n solved!')
