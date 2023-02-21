from time import sleep
import pyautogui as pg


headerMsg = """# TECH_IN_SECONDS

# Snake Game in Python using Pygame""".upper()


sleep(3)
pg.click(1000,500)

file = open("code.txt",'r')
code = file.read()
file.close()

filename = "Snake.py"
code = headerMsg + "\n\n" + code
file = open(filename,'w')
file.close()
sleep(1)

pg.hotkey("ctrl",'o')
sleep(2)
pg.typewrite(filename,0.09)
sleep(1)

pg.press("down")
pg.press("enter")
# sleep(2)
# pg.click(1000,500)

# pg.hotkey("win","alt","r")
pg.hotkey("shift","insert")
line = 0
sleep(4)
for ch in code:
    file = open(filename,"a")
    if ch == "\n":
        if line%22 == 21:
            for i in range(16):
                pg.scroll(-100)
                sleep(0.1)
        line = line + 1
    file.write(ch)
    sleep(0.1)
    file.close()


# sleep(4)
# pg.hotkey("win","alt","r")
