from time import sleep
import pyautogui as pg 

sleep(5)

for i in range(100):
    for j in range(500):
        pg.hotkey("ctrl","d")
    pg.press("right")
    pg.press("left")
    pg.press("enter")
    sleep(15)
