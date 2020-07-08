import tkinter as tk 
from tkinter import ttk
win = tk.Tk()
win.title("GUI")


# create labels
name_label = tk.Label(win, text="Enter your name :")
name_label.grid(row=0, column=0, sticky=tk.W)


email_label = tk.Label(win, text="Enter your email :")
email_label.grid(row=2, column=0, sticky=tk.W)


age_label = tk.Label(win, text="Enter your age :")
age_label.grid(row=1, column=0, sticky=tk.W)


# create entry box
name_var = tk.StringVar()
name_entrybox = tk.Entry(win, width=20, textvariable = name_var)
name_entrybox.grid(row=0, column=1)

email_var = tk.StringVar()
email_entrybox = tk.Entry(win, width=20, textvariable = email_var)
email_entrybox.grid(row=1, column=1)

age_var = tk.StringVar()
age_entrybox = tk.Entry(win, width=20, textvariable = age_var)
age_entrybox.grid(row=2, column=1)

# create combobox
gender_var = tk.StringVar() 
gender_combobox = ttk.Combobox(win, width=17, textvariable = gender_var)
gender_combobox["value"] = ("male", "female", "other",)
gender_combobox.grid(row=3, column=1)

# create radiobutton
usertype = tk.StringVar()
radiobtn1 = tk.Radiobutton(win, text="student", value="student", variable="usertype")
radiobtn1.grid(row=4, column=0)

usertype = tk.StringVar()
radiobtn2 = tk.Radiobutton(win, text="teacher", value="teacher", variable="usertype")
radiobtn2.grid(row=4, column=1)


# check button
checkbtn_var = tk.IntVar()
checkbtn = tk.Checkbutton(win, text="subscribe")
checkbtn.grid(row=5, column=0)


# create button
def action():
    username = name_var.get()
    userage = age_var.get()
    user_email = email_var.get()

    print(f"{username} is {user_email} years old, {userage}")
    user_gender = gender_var.get()
    usertype =  usertype_var.get()
    
    if checkbtn_var.get() == 0:
        subscribe = "NO"
    else:
        subscribe = "Yes"
    print(user_gender, user_type, subscribe)


submit_button = tk.Button(win, text="Submit", command=action)
submit_button.grid(row=3, column=0)

win.mainloop()