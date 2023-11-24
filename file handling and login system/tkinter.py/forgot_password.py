from tkinter import *
from tkinter import messagebox
import mysql.connector

window = Tk()

window.title("softini solution registration form")
window.geometry("600x450")
window.resizable(0, 0)

def submition():
    if usernameentry.get() == '':
        messagebox.showerror("Alert!", "please enter username")
    elif emailentry.get() == '':
        messagebox.showerror("Alert!", "please enter email")
    elif passwordentry.get() == '':
        messagebox.showerror("Alert!", "please enter password")
    elif confirmpasswordentry.get() == '':
        messagebox.showerror("Alert!", "please enter confirm password")
    else:
        db = mysql.connector.connect(host="localhost", user="root", password="", database="softini")
        cur = db.cursor()
        query = 'SELECT * FROM registeration WHERE email=%s'
        cur.execute(query, (emailentry.get(),))
        row = cur.fetchone()

        if row is None:
            messagebox.showerror("Alert", "This email does not exist")
            db.close()
            return
        else:
            query = 'UPDATE registeration SET password=%s WHERE email=%s'
            cur.execute(query, (passwordentry.get(), emailentry.get()))
            db.commit()
            db.close()
            messagebox.showinfo('Success', 'Password updated successfully')

def rem():
    window.destroy()
    import login

frame = Frame(window, width=800, height=650, bg="#5d1d88", bd=8)
frame.place(x=0, y=0)

heading = Label(frame, text="Forgot password", fg='#F4CE14', bg="#5d1d88", font=("Times New Roman", 40, "bold"))
heading.place(x=80, y=0)

username = Label(frame, text="Username :", fg='#F4CE14', bg="#5d1d88", font=("Times New Roman", 20, "bold"))
username.place(x=50, y=90)

usernameentry = Entry(frame, width=30, borderwidth=2)
usernameentry.place(x=380, y=100)

email = Label(frame, text="Email :", fg='#F4CE14', bg="#5d1d88", font=("Times New Roman", 20, "bold"))
email.place(x=50, y=150)

emailentry = Entry(frame, width=30, borderwidth=2)
emailentry.place(x=380, y=160)

password = Label(frame, text="New password :", fg='#F4CE14', bg="#5d1d88", font=("Times New Roman", 20, "bold"))
password.place(x=50, y=210)

passwordentry = Entry(frame, width=30, borderwidth=2)
passwordentry.place(x=380, y=220)

confirmpassword = Label(frame, text="Confirm new password :", fg='#F4CE14', bg="#5d1d88", font=("Times New Roman", 20, "bold"))
confirmpassword.place(x=50, y=280)

confirmpasswordentry = Entry(frame, width=30, borderwidth=2)
confirmpasswordentry.place(x=380, y=290)

submit = Button(frame, text="Submit", fg='#5d1d88', bg="#F4CE14",height=1,width=10,borderwidth=5, font=("Times New Roman", 20, "bold"),command=submition)
submit.place(x=200, y=380)

back=Button(frame, text="Remembered", fg='#5d1d88', bg="#F4CE14",height=1,width=10, font=("harrington", 10, "bold"),command=rem)
back.place(x=20,y=400)

window.mainloop()
