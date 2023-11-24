from tkinter import *
from tkinter import messagebox
import pymysql

window = Tk()

window.title("softini solution registeration form")
window.geometry("600x650+200+10")
window.resizable(0, 0)

def submit():
    if firstnameentry.get() == '' or lastnameentry.get() == '' or emailentry.get() == '' or om.get() == '' or usernameentry.get() == '' or passwordentry.get() == '' or confirmpasswordentry.get() == '':
        messagebox.showerror("Alert!", "Please fill in all the fields")
    else:
        db = None  # Initialize db outside the try block
        try:
            db = pymysql.connect(host="localhost", port=3306, user="root", password='1234')
            cur = db.cursor()

            # Create database if not exists
            cur.execute('CREATE DATABASE IF NOT EXISTS softni_solution_registration_form')
            cur.execute('USE softni_solution_registration_form')

            # Create users table if not exists
            cur.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    first_name VARCHAR(255),
                    last_name VARCHAR(255),
                    email VARCHAR(255),
                    country VARCHAR(255),
                    username VARCHAR(255),
                    password VARCHAR(255)
                )
            ''')

            # Check if the username already exists
            cur.execute('SELECT * FROM users WHERE username = %s', (usernameentry.get(),))
            existing_user = cur.fetchone()
            if existing_user:
                messagebox.showerror("Alert!", "Username already exists. Choose a different username.")
            else:
                # Insert user data into the table
                insert_query = '''
                    INSERT INTO users (first_name, last_name, email, country, username, password)
                    VALUES (%s, %s, %s, %s, %s, %s)
                '''
                data = (firstnameentry.get(), lastnameentry.get(), emailentry.get(), om.get(), usernameentry.get(), passwordentry.get())
                cur.execute(insert_query, data)
                db.commit()

                messagebox.showinfo("Successful Connection", "Registration Successful!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            # Close the database connection
            if db:
                db.close()

# ... (rest of your code)








def show1():
    passwordentry.configure(show='x')
    check1.configure(command=hide1)

def hide1():
    passwordentry.configure(show='')
    check1.configure(command=show1)


def show2():
    confirmpasswordentry.configure(show='x')
    check2.configure(command=hide2)

def hide2():
    confirmpasswordentry.configure(show='')
    check2.configure(command=show2)

firstname =StringVar()
lastname =StringVar()
email =StringVar()
gender=StringVar()
username =StringVar()
password =StringVar()
confirmpassword =StringVar()



om =StringVar()

frame = Frame(window,width=800 ,height=650,bg="#F4CE14",bd=8)
frame.place(x=0,y=0)

country =("Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic (Czechia)", "Democratic Republic of the Congo", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor (Timor-Leste)", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar (Burma)", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia (formerly Macedonia)", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe")
om.set("select country")



heading = Label (frame , text = "Softini solution",fg='#143d59',bg="#F4CE14",font=("Times New Roman",40,"bold"))
heading.place(x=100,y=3)
headings = Label (frame , text = "Registeration form",fg='#143d59',bg="#F4CE14",font=("Times New Roman",40,"bold"))
headings.place(x=70,y=60)

firstname = Label (frame , text = "First Name :",fg='#143d59',bg="#F4CE14",font=("Times New Roman",20,"bold"))
firstname.place(x=40,y=150)

firstnameentry = Entry(frame,width=30 , borderwidth=2)
firstnameentry.place(x=200,y=160)

lastname = Label (frame , text = "Last Name :",fg='#143d59',bg="#F4CE14",font=("Times New Roman",20,"bold"))
lastname.place(x=40,y=200)

lastnameentry = Entry(frame,width=30 , borderwidth=2)
lastnameentry.place(x=200,y=210)

email = Label (frame , text = "Email :",fg='#143d59',bg="#F4CE14",font=("Times New Roman",20,"bold"))
email.place(x=40,y=250)

emailentry = Entry(frame,width=30 , borderwidth=2)
emailentry.place(x=200,y=260)

gender = Label (frame , text = "Gender :",fg='#143d59',bg="#F4CE14",font=("Times New Roman",20,"bold"))
gender.place(x=40,y=300)


genderradio1 = Radiobutton (frame , text = "MALE",variable=gender,value="MALE",font=("Times New Roman",20,"bold"))
genderradio1.place(x=200,y=300)

genderradio2 = Radiobutton (frame , text = "FEMALE",variable=gender,value="FEMALE",font=("Times New Roman",20,"bold"))
genderradio2.place(x=350,y=300)

username = Label (frame , text = "User Name :",fg='#143d59',bg="#F4CE14",font=("Times New Roman",20,"bold"))
username.place(x=40,y=350)

usernameentry = Entry(frame,width=30 , borderwidth=2)
usernameentry.place(x=200,y=360)

password = Label (frame , text = "Password :",fg='#143d59',bg="#F4CE14",font=("Times New Roman",20,"bold"))
password.place(x=40,y=400)

passwordentry = Entry(frame,width=30 , borderwidth=2)
passwordentry.place(x=200,y=410)

confirmpasswords = Label (frame , text = "confirm Password :",fg='#143d59',bg="#F4CE14",font=("Times New Roman",20,"bold"))
confirmpasswords.place(x=40,y=450)

confirmpasswordentry = Entry(frame,width=30 , borderwidth=2)
confirmpasswordentry.place(x=305,y=460)

countrys = Label (frame , text = "Select Country :",fg='#143d59',bg="#F4CE14",font=("Times New Roman",20,"bold"))
countrys.place(x=40,y=510)

countrylabeldropdown= OptionMenu(frame,om, *country)
countrylabeldropdown.place(x=240,y=520)

check1 = Checkbutton(frame,text='',bg="#F4CE14",command=show1)
check1.place(x=390,y=410)

check2 = Checkbutton(frame,text='',bg="#F4CE14",command=show2)
check2.place(x=490,y=460)

subitionbtn=Button(frame,text='submit',bg="light blue",width=12 ,borderwidth=10,height=2,cursor="hand2",font=("Times New Roman",12,"bold"),command=submit)
subitionbtn.place(x=220,y=570)

bckbtn=Button(frame,text='<<',bg="light blue",width=12 ,borderwidth=5,height=2,cursor="hand2")
bckbtn.place(x=40,y=580)


window.mainloop()
