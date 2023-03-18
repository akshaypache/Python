from tkinter import * 
from tkinter.ttk import *
from tkcalendar import DateEntry
from tkinter import filedialog
import os
from datetime import datetime
import csv  
import shutil

uploadPhotoPath = ""
def upload_Photo():
    global uploadPhotoPath
    uploadPhotoPath = filedialog.askopenfilename()
    photoLbl.configure(text=uploadPhotoPath.split("/")[-1])
    
uploadSignPath = ""
def upload_Sign():
    global uploadSignPath
    uploadSignPath = filedialog.askopenfilename()
    signLbl.configure(text=uploadSignPath.split("/")[-1])

def Clear():
    fNameEntryVar.set("")
    mNameEntryVar.set("")
    lNameEntryVar.set("")
    courseEntryVar.set("")
    fromEntryVar.set("")
    toEntryVar.set("")
    gradeEntryVar.set("")
    phoneEntryVar.set("")
    emailEntryVar.set("")
    adharEntryVar.set("")
    photoLbl.configure(text="Passport Photo")
    signLbl.configure(text="Sign")

def Submit():
    now = datetime.now()
    date = now.strftime("%d%B%Y")
    try:
        os.mkdir(date)
    except:
        pass 

    fNameEntryTxt = fNameEntryVar.get()
    mNameEntryTxt = mNameEntryVar.get()
    lNameEntryTxt = lNameEntryVar.get()
    courseEntryTxt = courseEntryVar.get()
    fromEntryTxt = fromEntryVar.get()
    toEntryTxt = toEntryVar.get()
    gradeEntryTxt = gradeEntryVar.get()
    phoneEntryTxt = phoneEntryVar.get()
    emailEntryTxt = emailEntryVar.get()
    adharEntryTxt = adharEntryVar.get()

    csvFile = open(f"{date}/data.csv","a",newline="")
    writer = csv.writer(csvFile)
    writer.writerow([fNameEntryTxt,mNameEntryTxt,lNameEntryTxt,courseEntryTxt,fromEntryTxt,toEntryTxt,gradeEntryTxt,phoneEntryTxt,emailEntryTxt,adharEntryTxt,uploadPhotoPath,uploadSignPath])
    csvFile.close()
    shutil.copyfile(uploadPhotoPath, f"{date}/photo.png")
    shutil.copyfile(uploadSignPath, f"{date}/sign.png")


    fNameEntryVar.set("")
    mNameEntryVar.set("")
    lNameEntryVar.set("")
    courseEntryVar.set("")
    fromEntryVar.set("")
    toEntryVar.set("")
    gradeEntryVar.set("")
    phoneEntryVar.set("")
    emailEntryVar.set("")
    adharEntryVar.set("")
    photoLbl.configure(text="Passport Photo")
    signLbl.configure(text="Sign")


root = Tk(className = " ALL INDIA PROFESSIONAL SKILL CERTIFICATION COUNCIL")
# root.resizable(0,0)
headF = Frame(root,relief=SUNKEN,padding=20)
headF.pack(fill = X, expand = False,anchor="ne")
b1 = Label(headF, text = "ALL INDIA PROFESSIONAL SKILL CERTIFICATION COUNCIL",font=("Bold",30),anchor=S)
b1.pack(fill = X, expand = True)


fNameEntryVar = StringVar()
mNameEntryVar = StringVar()
lNameEntryVar = StringVar()
courseEntryVar = StringVar()
fromEntryVar = StringVar()
toEntryVar = StringVar()
gradeEntryVar = StringVar()
phoneEntryVar = StringVar()
emailEntryVar = StringVar()
adharEntryVar = StringVar()


bodyF = Frame(root)
bodyF.pack(fill = BOTH, expand = True)


bodyRightFram = Frame(bodyF,height=200,width=500,padding=50,relief=SUNKEN)
bodyRightFram.pack(fill = BOTH, expand = True,side=RIGHT)

bodyLeftFram = Frame(bodyF,height=200,width=500,padding=50,relief=SUNKEN)
bodyLeftFram.pack(fill = BOTH, expand = True,side=LEFT)


fNameLbl = Label(bodyLeftFram, text = "First Name",font=("Bold",15))
fNameLbl.pack(fill = BOTH, expand = True)
fNameEntry = Entry(bodyLeftFram,justify=RIGHT,font=("Bold",20),textvariable=fNameEntryVar)
fNameEntry.pack(fill = BOTH, expand = True)

mNameLbl = Label(bodyLeftFram, text = "Middle Name",font=("Bold",15))
mNameLbl.pack(fill = BOTH, expand = True)
mNameEntry = Entry(bodyLeftFram,justify=RIGHT,font=("Bold",20),textvariable=mNameEntryVar)
mNameEntry.pack(fill = BOTH, expand = True)

lNameLbl = Label(bodyLeftFram, text = "Last Name",font=("Bold",15))
lNameLbl.pack(fill = BOTH, expand = True)
lNameEntry = Entry(bodyLeftFram,justify=RIGHT,font=("Bold",20),textvariable=lNameEntryVar)
lNameEntry.pack(fill = BOTH, expand = True)

courseLbl = Label(bodyLeftFram, text = "Course",font=("Bold",15))
courseLbl.pack(fill = BOTH, expand = True)
courseEntry = Entry(bodyLeftFram,justify=RIGHT,font=("Bold",20),textvariable=courseEntryVar)
courseEntry.pack(fill = BOTH, expand = True)

dateFram = Frame(bodyLeftFram)
dateFram.pack(fill = BOTH, expand = True)

fromLbl = Label(dateFram, text = "From",width=18,  font=("Bold",15),justify=LEFT)
fromLbl.grid(row=0,column=0,padx=15,pady=10)

fromEntry = DateEntry(dateFram,font=("Bold",20),justify=RIGHT,date_pattern='dd-MM-yyyy',textvariable=fromEntryVar)
fromEntry.grid(row=1,column=0)

toLbl = Label(dateFram, text = "To",width=18,font=("Bold",15),justify=LEFT)
toLbl.grid(row=0,column=1,padx=15,pady=10)
toEntry = DateEntry(dateFram,font=("Bold",20),justify=RIGHT,date_pattern='dd-MM-yyyy',textvariable=toEntryVar)
toEntry.grid(row=1,column=1)




gradeLbl = Label(bodyLeftFram, text = "Grade",font=("Bold",15))
gradeLbl.pack(fill = BOTH, expand = True)
options = ["Select Grade","A Grade","B Grade","C Grade","D Grade","A+ Grade","B+ Grade","C+ Grade","D+ Grade",]
gradeEntry = OptionMenu(bodyLeftFram,gradeEntryVar, *options,direction="right")
gradeEntry.pack(fill = BOTH, expand = True)

phoneLbl = Label(bodyRightFram, text = "Phone",font=("Bold",15))
phoneLbl.pack(fill = BOTH, expand = True)
phoneEntry = Entry(bodyRightFram,justify=RIGHT,font=("Bold",20),textvariable=phoneEntryVar)
phoneEntry.pack(fill = BOTH, expand = True)

emailLbl = Label(bodyRightFram, text = "Email",font=("Bold",15))
emailLbl.pack(fill = BOTH, expand = True)
emailEntry = Entry(bodyRightFram,justify=RIGHT,font=("Bold",20),textvariable=emailEntryVar)
emailEntry.pack(fill = BOTH, expand = True)

adharLbl = Label(bodyRightFram, text = "Aadhaar No",font=("Bold",15))
adharLbl.pack(fill = BOTH, expand = True)
adharEntry = Entry(bodyRightFram,justify=RIGHT,font=("Bold",20),textvariable=adharEntryVar)
adharEntry.pack(fill = BOTH, expand = True)


BtnFram = Frame(bodyRightFram)
BtnFram.pack(fill = BOTH, expand = True)

photoLbl = Label(BtnFram, text = "Passport Photo",font=("Bold",15))
photoLbl.grid(row=0, column=0)
photoBtn = Button(BtnFram,text="Select Photo",width=40,padding=20,command = lambda:upload_Photo())
photoBtn.grid(row=1, column=0)

signLbl = Label(BtnFram, text = "Sign",font=("Bold",15))
signLbl.grid(row=0, column=1)
signBtn = Button(BtnFram,text="Select Sign",width=40,padding=20,command = lambda:upload_Sign())
signBtn.grid(row=1, column=1)
 
clear_button = Button(BtnFram, text="Clear",width=40,padding=20,command=Clear)
clear_button.grid(row=2,column=0,padx=10,pady=10)
submit_button = Button(BtnFram, text="Submit",width=40,padding=20,command=Submit)
submit_button.grid(row=2,column=1,padx=10,pady=10)



root.mainloop()

