import pyautogui as pi
from time import sleep

pi.PAUSE = 1.0


sleep(6)
for i in range(130):
    pi.click(x=1479, y=184)

    pi.click(x=1541, y=321)

    pi.press('right')


