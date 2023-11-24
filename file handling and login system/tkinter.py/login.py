from tkinter import *
from tkinter import messagebox
import mysql.connector

window = Tk()

window.title("softini solution registration form")
window.geometry("600x250")
window.resizable(0, 0)

connection = mysql.connector.connect(host="localhost", user="root", password="", database="softini")
c = connection.cursor()


def login():
    if usernameentry.get() == '':
        messagebox.showerror("Alert!", "please enter email")
    elif passwordentry.get() == '':
        messagebox.showerror("Alert!", "please enter password") 
    else: 
        query = 'SELECT * FROM registeration WHERE email=%s AND password=%s'
        c.execute(query, (usernameentry.get(), passwordentry.get()))
        row = c.fetchone()
        if row is None:
            messagebox.showerror('Alert', 'Incorrect email or password')
        else:
            messagebox.showinfo('Success', 'Login Successfully')

def next():
    window.destroy()
    import tikinter

def forget():
    window.destroy()
    import forgot_password
frame = Frame(window, width=800, height=650, bg="#5d1d88", bd=8)
frame.place(x=0, y=0)

username = Label(frame, text="Email :", fg='#F4CE14', bg="#5d1d88", font=("Times New Roman", 20, "bold"))
username.place(x=80, y=10)

usernameentry = Entry(frame, width=30, borderwidth=2)
usernameentry.place(x=240, y=20)

password = Label(frame, text="Password:", fg='#F4CE14', bg="#5d1d88", font=("Times New Roman", 20, "bold"))
password.place(x=80, y=70)

passwordentry = Entry(frame, width=30, borderwidth=2, show="*") 
passwordentry.place(x=240, y=80)

passworde = Label(frame, text="Don't have an account ?", fg='#F4CE14', bg="#5d1d88", font=("harrington", 9, "bold"))
passworde.place(x=4, y=170)

passworde = Button(frame, text="Forgot password ?", fg='#F4CE14', bg="#5d1d88", font=("harrington", 9, "bold"),command=forget)
passworde.place(x=300, y=105)

createbtn = Button(frame, text='Create One', bg='#F4CE14', fg="#5d1d88", width=10, borderwidth=5, height=1,
font=("Times New Roman", 12, "bold"), command=next)
createbtn.place(x=10, y=190)

submissionbtn = Button(frame, text='Login', bg='#F4CE14', fg='#5d1d88', width=20, borderwidth=5, height=2,
font=("Times New Roman", 12, "bold"), command=login)
submissionbtn.place(x=240, y=170)

window.mainloop()

