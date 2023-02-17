from time import sleep 
import pyautogui as pg 

sleep(4)

file = open("code.py","r")
data = file.read().split("\n")
file.close()

for i in data:
    pg.typewrite(i,0.08)
    pg.hotkey("shift","enter")


    

