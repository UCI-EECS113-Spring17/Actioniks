from pynq import Overlay
from pynq.iop import Pmod_OLED
from pynq.iop import PMODA

ol = Overlay("base.bit")
ol.download()

pmod_oled = Pmod_OLED(PMODA)

pmod_oled.clear()
pmod_oled.write('I love Pynq')
