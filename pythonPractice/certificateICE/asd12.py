import tkinter as tk

def submit_form():
    # retrieve input values from form
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    
    # do something with the input data, such as saving to a database
    print(f"Name: {name}\nAge: {age}\nEmail: {email}")
    
    # clear form fields
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# create tkinter window
root = tk.Tk()
root.title("Data Entry Form")

# create form labels and entries
name_label = tk.Label(root, text="Name:",font=("bold",18))
name_entry = tk.Entry(root,font=("bold",18))
age_label = tk.Label(root, text="Age:",font=("bold",18))
age_entry = tk.Entry(root,font=("bold",18))
email_label = tk.Label(root, text="Email",font=("bold",18))
email_entry = tk.Entry(root,font=("bold",18))

name_label1 = tk.Label(root, text="Name:",font=("bold",18))
name_entry1 = tk.Entry(root,font=("bold",18))
age_label1 = tk.Label(root, text="Age:",font=("bold",18))
age_entry1 = tk.Entry(root,font=("bold",18))
email_label1 = tk.Label(root, text="Email",font=("bold",18))
email_entry1 = tk.Entry(root,font=("bold",18))

name_label2 = tk.Label(root, text="Name:",font=("bold",18))
name_entry2 = tk.Entry(root,font=("bold",18))
age_label2 = tk.Label(root, text="Age:",font=("bold",18))
age_entry2 = tk.Entry(root,font=("bold",18))
email_label2 = tk.Label(root, text="Email",font=("bold",18))
email_entry2 = tk.Entry(root,font=("bold",18))

# create submit button
submit_button = tk.Button(root, text="Submit",font=("bold",18), command=submit_form)

# layout form elements
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
age_label.grid(row=1, column=0)
age_entry.grid(row=1, column=1)
email_label.grid(row=2, column=0)
email_entry.grid(row=2, column=1)
name_label1.grid(row=3, column=0)
name_entry1.grid(row=3, column=1)
age_label1.grid(row=4, column=0)
age_entry1.grid(row=4, column=1)
email_label1.grid(row=5, column=0)
email_entry1.grid(row=5, column=1)
name_label2.grid(row=6, column=0)
name_entry2.grid(row=6, column=1)
age_label2.grid(row=7, column=0)
age_entry2.grid(row=7, column=1)
email_label2.grid(row=8, column=0)
email_entry2.grid(row=8, column=1)


submit_button.grid(row=9, column=1)

# start the main loop
root.mainloop()
