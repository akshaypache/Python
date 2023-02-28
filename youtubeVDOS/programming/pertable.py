import tkinter as tk
from elementsData import elementInfo,elements

root = tk.Tk()
root.title("Periodic Table")
root.configure(bg="grey7")
root.resizable(0,0)

mainframe = tk.Frame(root,bg="grey7")
mainframe.pack()

def info(event):
    outputWindow = tk.Tk()
    outputWindow.configure(bg="grey7")
    outputWindow.resizable(0,0)

    def des():
        outputWindow.destroy()


    text = event.widget.cget("text").split("\n")[1]
    for ele in elementInfo:
        var = ele.split(",")
        if text in var[0]:
            EleInfo = ele.split(",")
            list = ["Atomic number", "Relative atomic mass", "Standard state", "Classification", "Group", "Group name", "Period", "Block", "Shell structure", "CAS Registry"]
            
            for i in range(10):
                outputWindow.title(f"This information about {EleInfo[0]}")

                b1Btn = tk.Button(outputWindow,
                                text= list[i].upper(),
                                bg="grey7",
                                fg="white",
                                font=("Arial", 20,"bold"),
                                height=1,
                                width=30)
                b1Btn.grid(row=i,column=0)
                
                b2Btn = tk.Button(outputWindow,
                                text= EleInfo[i+1],
                                bg="grey7",
                                fg="white",
                                font=("Arial", 20,"bold"),
                                height=1,
                                width=30)
                b2Btn.grid(row=i,column=1)

            bkBtn = tk.Button(outputWindow,
                                text= "Back",
                                bg="grey7",
                                fg="red",
                                font=("Arial", 20,"bold"),
                                height=2,
                                width=30,
                                command=des)
            bkBtn.grid(row=10,column=0,columnspan=2)
    outputWindow.mainloop()


for element in elements:
    button = tk.Button(
        mainframe,
        text=f"{element['symbol']}\n{element['name']}",
        width=11,
        height=3,
        bg="blue",
        fg = "white",
        font=("Arial", 10,"bold"),
        borderwidth=1,
        relief="solid",
    )
    button.grid(row=element["row"], column=element["col"])
    button.bind("<Button-1>", info)

button = tk.Button(
        mainframe,
        text="Periodic Table",
        width=20,
        height=2,
        bg="grey7",
        fg = "white",
        font=("Arial", 30,"bold"),
        borderwidth=1,
        relief="solid",
    )
button.grid(row=1, column=5,columnspan=7,rowspan=3)
# button.bind("<Button-1>", infomy)


root.mainloop()