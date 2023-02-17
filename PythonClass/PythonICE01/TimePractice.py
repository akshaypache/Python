# https://www.programiz.com/python-programming/datetime/strftime

# import time 

# print("Hello")
# time.sleep(2)
# print("Hello")


# for i in range(11):
#     print(f"NASA Hacked {i*10}%")
#     time.sleep(1)
# print("ACCESS GRANTED")


# import os
# from datetime import datetime

# now = datetime.now()
# print(now)

# 16-02-2023

# a = now.strftime("DATE : %d / %m / %Y")
# print(a)



# ===================================




import os
from datetime import datetime
import time 

while(True):
    os.system("cls")
    now = datetime.now()
    a = now.strftime("%I : %M : %S : %f %p")
    print(a)
    time.sleep(1)




# import calendar

# a = calendar.month(2023,5)
# print(a)

# a = calendar.calendar(2023)
# print(a)

# a = calendar.weekday(2023,2,16)

# day = {
#     0 : "Monday", 
#     1 : "Tueday", 
#     2 : "Wednesday", 
#     3 : "Thursday", 
#     4 : "Friday", 
#     5 : "Saturday", 
#     6 : "Sunday", 
# }

# print(day[a])