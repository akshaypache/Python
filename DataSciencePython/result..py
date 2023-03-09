import pyautogui as pg
from time import sleep

roll = [
790692, 790742, 790744, 790745, 790747, 790748, 790749, 790750, 790751, 790752, 790753, 790754, 790755, 790922, 790923, 790924, 790925, 790926, 790928, 790929, 790947, 790948, 790949, 790950, 790951, 790952, 790953, 790954, 790955, 790956, 790957, 790958, 790959, 790960, 790961, 790962, 790963, 790964, 790965, 790966, 790967, 790968, 790980, 790981, 790983, 790986, 790987, 790988, 790991, 790992, 790993, 790995, 790996, 790998, 790999, 791000, 791007, 791008, 791009, 791011, 791012, 791013, 791014, 791015, 791016, 791017, 791018, 791019, 791020, 791021, 791022, 791023, 791024, 791025, 791026, 791027, 791028, 791029, 791031, 791032]

# a = pg.position()
# sleep(2)
print(len(roll))
exit()

for i in roll:
    # select faculty
    pg.click(262,578)
    sleep(1)
    # faculty of humanities
    pg.click(362,645)
    sleep(2)
    # select exam
    pg.click(362,645)
    sleep(2)

    # scroll examlist 
    pg.click(582,1054,clicks=7,interval=0.3)
    sleep(1)
    # select 3rd bvoc
    pg.click(438,957)
    sleep(1)
    # click roll number
    pg.click(228,727)
    pg.click(228,727)
    sleep(1)
    # type roll
    pg.typewrite(str(i),0.1)
    sleep(1)
    # view result
    pg.click(115,777)
    sleep(3)

    pg.rightClick(300,350)
    sleep(1)
    
    pg.click(395,395)
    sleep(3)

    pg.typewrite(str(i),0.1)
    sleep(1)
    
    pg.press("enter")
    sleep(1)

    pg.hotkey("ctrl","w")
    sleep(1)

    pg.hotkey("ctrl","t")
    sleep(1)

    pg.hotkey("ctrl","e")
    sleep(1)

    pg.press("backspace")
    sleep(1)

    pg.typewrite("https://rtmnuresults.org/",0.1)
    sleep(1)

    pg.press("enter")
    sleep(4)


