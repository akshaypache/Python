from time import sleep 
import pyautogui as pg 

sleep(3)

file = open("data.txt","r")
data = file.read().split("\n")
file.close()

for i in data:
    pg.typewrite(i,0.08)
    pg.hotkey("shift","enter")


    

