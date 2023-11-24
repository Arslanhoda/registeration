from tkinter import *
from tkinter import messagebox
import mysql.connector

window = Tk()

window.title("softini solution registeration form")
window.geometry("600x650+200+10")
window.resizable(0, 0)
connection = mysql.connector.connect(host="localhost", user="root", password="", database="softini")
c = connection.cursor()


def submit():
    if firstnameentry.get() == '':
        messagebox.showerror("Alert!", "please enter first name")
    elif lastnameentry.get() == '':
        messagebox.showerror("Alert!", "please enter last name")
    elif emailentry.get() == '':
        messagebox.showerror("Alert!", "please enter email")
    elif om.get() == 'select country':
        messagebox.showerror("Alert!", "please select country")
    elif oms.get() == 'select gender':
        messagebox.showerror("Alert!", "please select gender")
    elif usernameentry.get() == '':
        messagebox.showerror("Alert!", "please enter user name")
    elif passwordentry.get() == '':
        messagebox.showerror("Alert!", "please enter password")
    elif confirmpasswordentry.get() == '':
        messagebox.showerror("Alert!", "please enter confirmpassword")
    else:
        fname = firstnameentry.get()
        lname = lastnameentry.get()
        email = emailentry.get()
        gender = oms.get()
        username = usernameentry.get()
        password = passwordentry.get()
        confirmpassword = confirmpasswordentry.get()
        country = om.get()

        insert_query = "INSERT INTO `registeration`(`first name`, `last name`, `email`, `gender`, `username`, `password`, `confirm password`, `country`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        vals = (fname, lname, email, gender, username, password, confirmpassword, country)
        c.execute(insert_query, vals)
        connection.commit()
        messagebox.showinfo("Success", "Registration successful!")


def nextone():
    window.destroy()
    import login

def show1():
    passwordentry.configure(show='*')
    check1.configure(command=hide1)


def hide1():
    passwordentry.configure(show='')
    check1.configure(command=show1)


def show2():
    confirmpasswordentry.configure(show='*')
    check2.configure(command=hide2)


def hide2():
    confirmpasswordentry.configure(show='')
    check2.configure(command=show2)


firstname = StringVar()
lastname = StringVar()
email = StringVar()
oms = StringVar()
username = StringVar()
password = StringVar()
confirmpassword = StringVar()

om = StringVar()

frame = Frame(window, width=800, height=650, bg="#5d1d88", bd=8)
frame.place(x=0, y=0)

genders = ("Male", "Female", "central")
country = ("select country", "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda",
           "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh",
           "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina",
           "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", " Pakistan ", "Cambodia",
           "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros",
           "Congo", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic (Czechia)",
           "Democratic Republic of the Congo", "Denmark", "Djibouti", "Dominica", "Dominican Republic",
           "East Timor (Timor-Leste)", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia",
           "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana",
           "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary",
           "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Ivory Coast", "Jamaica",
           "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia",
           "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar",
           "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico",
           "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar (Burma)",
           "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea",
           "North Macedonia (formerly Macedonia)", "Norway", "Oman", "Cabo Verde", "Palau", "Panama",
           "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia",
           "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino",
           "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore",
           "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan", "Spain",
           "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania",
           "Thailand", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda",
           "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu",
           "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe")
om.set("select country")
oms.set("select gender")

heading = Label(frame, text="Softini solution", bg='#5d1d88', fg="#F4CE14", font=("Times New Roman", 40, "bold"))
heading.place(x=100, y=3)
headings = Label(frame, text="Registration form", bg='#5d1d88', fg="#F4CE14", font=("Times New Roman", 40, "bold"))
headings.place(x=70, y=60)

firstname = Label(frame, text="First Name :", bg='#5d1d88', fg="#F4CE14", font=("Times New Roman", 20, "bold"))
firstname.place(x=40, y=150)

firstnameentry = Entry(frame, width=30, borderwidth=2)
firstnameentry.place(x=200, y=160)

lastname = Label(frame, text="Last Name :", bg='#5d1d88', fg="#F4CE14", font=("Times New Roman", 20, "bold"))
lastname.place(x=40, y=200)

lastnameentry = Entry(frame, width=30, borderwidth=2)
lastnameentry.place(x=200, y=210)

email = Label(frame, text="Email :", bg='#5d1d88', fg="#F4CE14", font=("Times New Roman", 20, "bold"))
email.place(x=40, y=250)

emailentry = Entry(frame, width=30, borderwidth=2)
emailentry.place(x=200, y=260)

gender = Label(frame, text="Gender :", bg='#5d1d88', fg="#F4CE14", font=("Times New Roman", 20, "bold"))
gender.place(x=40, y=300)

genderlabeldropdown = OptionMenu(frame, oms, *genders)
genderlabeldropdown.place(x=200, y=310)

username = Label(frame, text="User Name :", bg='#5d1d88', fg="#F4CE14", font=("Times New Roman", 20, "bold"))
username.place(x=40, y=350)

usernameentry = Entry(frame, width=30, borderwidth=2)
usernameentry.place(x=200, y=360)

password = Label(frame, text="Password :", bg='#5d1d88', fg="#F4CE14", font=("Times New Roman", 20, "bold"))
password.place(x=40, y=400)

passwordentry = Entry(frame, width=30, borderwidth=2, show='*')
passwordentry.place(x=200, y=410)

confirmpasswords = Label(frame, text="Confirm Password :", bg='#5d1d88', fg="#F4CE14",
font=("Times New Roman", 20, "bold"))
confirmpasswords.place(x=40, y=450)

confirmpasswordentry = Entry(frame, width=30, borderwidth=2, show='*')
confirmpasswordentry.place(x=305, y=460)
countrys = Label(frame, text="Select Country :", bg='#5d1d88', fg="#F4CE14", font=("Times New Roman", 20, "bold"))
countrys.place(x=40, y=510)

countrylabeldropdown = OptionMenu(frame, om, *country)
countrylabeldropdown.place(x=240, y=520)

check1 = Checkbutton(frame, text='', bg="#5d1d88", command=show1)
check1.place(x=390, y=410)

check2 = Checkbutton(frame, text='', bg="#5d1d88", command=show2)
check2.place(x=490, y=460)

submissionbtn = Button(frame, text='Submit', bg="#F4CE14", width=12, borderwidth=10, height=2, cursor="hand2",
font=("Times New Roman", 12, "bold"), command=submit)
submissionbtn.place(x=220, y=570)

bckbtn = Button(frame, text='<<', bg="#F4CE14", width=12, borderwidth=5, height=2, cursor="hand2",command=nextone)
bckbtn.place(x=40, y=580)

window.mainloop()
