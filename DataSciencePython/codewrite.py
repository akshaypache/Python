from time import sleep 
import pyautogui as pg 

sleep(4)

file = open("code.txt","r")
data = file.read().split("\n")
file.close()

for i in data:
    pg.typewrite(i)
    pg.hotkey("shift","enter")


