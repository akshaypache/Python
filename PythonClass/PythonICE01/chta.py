import pyautogui as pg
from time import sleep 


sleep(3)
msg = "tuj zal ka j1".upper().replace(' ','.')

for i in msg:
    pg.typewrite(f"*{i}*",0.08)
    pg.press("enter")