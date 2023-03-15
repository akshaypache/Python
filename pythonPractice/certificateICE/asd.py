import tkinter as tk
from tkinter import filedialog
from PIL import  ImageTk

my_w = tk.Tk()
l1 = tk.Label(my_w,text='Add Student Data with Photo',width=30)  
l1.grid(row=1,column=1)
b1 = tk.Button(my_w, text='Upload File', width=20,command = lambda:upload_file())
b1.grid(row=2,column=1) 

def upload_file():
    global img
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = ImageTk.PhotoImage(file=filename)
    b2 =tk.Button(my_w,image=img) 
    b2.grid(row=3,column=1)

my_w.mainloop() 