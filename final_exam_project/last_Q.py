# ahmadreza zabihi chashmi   S.N=400521342

import sqlite3
import tkinter as tk
from tkinter import ttk , Canvas, messagebox
from PIL import ImageTk, Image


win = tk.Tk()

f0 = tk.Frame(win)
f0.grid(row=0,column=0,rowspan=7)

im = Canvas(f0, width=248, height=348)
im.pack()

img = ImageTk.PhotoImage(Image.open("arm.jpg"))
im.create_image(150,200, image=img)

text1 = ttk.Label(win, text="پست الکترونیکی دانشگاه علم و صنعت ایران")
text1.grid(row=0, column=1, sticky=tk.E)

text2 = ttk.Label(win, text="User name:")
text2.grid(row=1, column=1,sticky=tk.W)

user_name = tk.StringVar()
user_name_entered = ttk.Entry(win, width=20, textvariable=user_name)
user_name_entered.grid(column=1, row=2,sticky=tk.W)
user_name_entered.focus()

text3 = ttk.Label(win, text= "password:")
text3.grid(row=3, column=1,sticky=tk.W)

passs = tk.StringVar()
passs_en = ttk.Entry(win, width=20, textvariable=passs)
passs_en.grid(row=4, column=1,sticky=tk.W)

cheek = tk.IntVar()
cheek_e = ttk.Checkbutton(win, text="Use the light version of outlook web app")
cheek_e.grid(row=5,column=1, sticky=tk.W)


def sign_c():
    pasword = passs.get()
    us_er = user_name.get()
    if pasword=="" or us_er=="":
        messagebox.showerror("no entered", "enter User name and password")
    else:
        con = sqlite3.connect("second_Q.db")
        cur = con.cursor()
        cur.execute("SELECT username FROM users")
        usernames = [x[0] for x in cur.fetchall()]
        if not (us_er in usernames):
            user_name_entered.delete(0, "end")
            passs_en.delete(0, "end")
            messagebox.showerror("iust", "Log-in Failed!  Please Try Again!")
            con.close()
            return
        cur.execute("SELECT password FROM users WHERE username = ?", (us_er,))
        password = cur.fetchone()[0]
        if password != pasword:
            user_name_entered.delete(0, "end")
            passs_en.delete(0, "end")
            messagebox.showerror("iust", "Log-in Failed!  Please Try Again!")
            con.close()
            return
        messagebox.showinfo("iust", "You signed in")

        # text1.destroy()
        # text2.destroy()
        # text3.destroy()
        # passs_en.destroy()
        # cheek_e.destroy()
        # user_name_entered.destroy()
        # sign.destroy()
        # new_text = ttk.Label(win, text=" welcome to IUST ")
        # new_text.grid(row=3, column=1,padx=10)

sign = ttk.Button(win, text = " sign in " , command = sign_c ) 
sign.grid(column = 1, row = 6, sticky = tk.W)

win.mainloop()

