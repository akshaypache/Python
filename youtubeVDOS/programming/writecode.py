from time import sleep
import pyautogui as pg

file = open("code.txt",'r')
code = file.read()
file.close()

filename = "Snake.py"


pg.hotkey("ctrl",'o')
sleep(2)
pg.typewrite(filename,0.09)
sleep(1)
pg.press("enter")

for ch in code:
    file = open(filename,"a")
    file.write(ch)
    sleep(0.1)
    file.close()
