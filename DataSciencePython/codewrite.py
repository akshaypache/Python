from time import sleep 
import pyautogui as pg 
sleep(4)

file = open("code.txt","r")
data = file.read().split("\n")
file.close()

for i in data:
    pg.typewrite(i)
    pg.hotkey("shift","enter")




# for i in range(7):
#     for j in range(7):
#         if abs(i-3) + abs(j-3) <= 3:
#             print(5 - abs(i-3) - abs(j-3), end="")
#         else:
#             print(end=" ")
#     print()
