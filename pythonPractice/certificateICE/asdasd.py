from tkinter import * 
from tkinter.ttk import *
from tkcalendar import DateEntry


root = Tk()
# root.resizable(0,0)
headF = Frame(root,relief=SUNKEN,padding=20)
headF.pack(fill = X, expand = False,anchor="ne")
b1 = Label(headF, text = "ALL INDIA PROFESSIONAL SKILL CERTIFICATION COUNCIL",font=("Bold",30),anchor=S)
b1.pack(fill = X, expand = True)


bodyF = Frame(root)
bodyF.pack(fill = BOTH, expand = True)


bodyRightFram = Frame(bodyF,height=200,width=500,padding=50,relief=SUNKEN)
bodyRightFram.pack(fill = BOTH, expand = True,side=RIGHT)

bodyLeftFram = Frame(bodyF,height=200,width=500,padding=50,relief=SUNKEN)
bodyLeftFram.pack(fill = BOTH, expand = True,side=LEFT)

fNameLbl = Label(bodyLeftFram, text = "First Name",font=("Bold",15))
fNameLbl.pack(fill = BOTH, expand = True)
fNameEntry = Entry(bodyLeftFram,justify=CENTER,font=("Bold",20))
fNameEntry.pack(fill = BOTH, expand = True)

mNameLbl = Label(bodyLeftFram, text = "Middle Name",font=("Bold",15))
mNameLbl.pack(fill = BOTH, expand = True)
mNameEntry = Entry(bodyLeftFram,justify=CENTER,font=("Bold",20))
mNameEntry.pack(fill = BOTH, expand = True)

lNameLbl = Label(bodyLeftFram, text = "Last Name",font=("Bold",15))
lNameLbl.pack(fill = BOTH, expand = True)
lNameEntry = Entry(bodyLeftFram,justify=CENTER,font=("Bold",20))
lNameEntry.pack(fill = BOTH, expand = True)

courseLbl = Label(bodyLeftFram, text = "Course",font=("Bold",15))
courseLbl.pack(fill = BOTH, expand = True)
courseEntry= Entry(bodyLeftFram,justify=CENTER,font=("Bold",20))
courseEntry.pack(fill = BOTH, expand = True)

fromLbl = Label(bodyLeftFram, text = "From",  font=("Bold",15))
fromLbl.pack(fill = BOTH, expand = True)
fromEntry = DateEntry(bodyLeftFram,font=("Bold",20),justify=CENTER,date_pattern='MM-dd-yyyy')
fromEntry.pack(fill = BOTH, expand = True)

toLbl = Label(bodyLeftFram, text = "To",font=("Bold",15))
toLbl.pack(fill = BOTH, expand = True)
toEntry = DateEntry(bodyLeftFram,font=("Bold",20),justify=CENTER,date_pattern='MM-dd-yyyy')
toEntry.pack(fill = BOTH, expand = True)




clicked = StringVar()
gradeLbl = Label(bodyRightFram, text = "Grade",font=("Bold",15))
gradeLbl.pack(fill = BOTH, expand = True)
options = ["Select Grade","A Grade","B Grade","C Grade","D Grade","A+ Grade","B+ Grade","C+ Grade","D+ Grade",]
gradeEntry = OptionMenu(bodyRightFram,clicked, *options)
# clicked.set( "s Grade" )
gradeEntry.pack(fill = BOTH, expand = True)

phoneLbl = Label(bodyRightFram, text = "Phone",font=("Bold",15))
phoneLbl.pack(fill = BOTH, expand = True)
phoneEntry = Entry(bodyRightFram,justify=CENTER,font=("Bold",20))
phoneEntry.pack(fill = BOTH, expand = True)

emailLbl = Label(bodyRightFram, text = "Email",font=("Bold",15))
emailLbl.pack(fill = BOTH, expand = True)
emailEntry = Entry(bodyRightFram,justify=CENTER,font=("Bold",20))
emailEntry.pack(fill = BOTH, expand = True)

adharLbl = Label(bodyRightFram, text = "Aadhaar No",font=("Bold",15))
adharLbl.pack(fill = BOTH, expand = True)
adharEntry = Entry(bodyRightFram,justify=CENTER,font=("Bold",20))
adharEntry.pack(fill = BOTH, expand = True)

photoLbl = Label(bodyRightFram, text = "Photo",font=("Bold",15))
photoLbl.pack(fill = BOTH, expand = True)
photoEntry = Entry(bodyRightFram,justify=CENTER,font=("Bold",20))
photoEntry.pack(fill = BOTH, expand = True)

signLbl = Label(bodyRightFram, text = "Sign",font=("Bold",15))
signLbl.pack(fill = BOTH, expand = True)
signEntry = Entry(bodyRightFram,justify=CENTER,font=("Bold",20))
signEntry.pack(fill = BOTH, expand = True)



root.mainloop()
