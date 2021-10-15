import tkinter
from tkinter import *
from tkinter import messagebox
import re
import string
import random

class User:
    flag = 0
    index = 0
    flag_f = 0

    def __init__(self,email, password):
        self.email = email
        self.password = password


    def validate_email(self):
        if not(self.flag_f):
            reg_ex = r'\b[A-Za-z0-9]+@+[a-z]+\.[A-Z|a-z]{2,}\b'
            if re.match(reg_ex, self.email):
                with open("log.txt","a") as f:
                    f.write(self.email+" ")
                    self.flag = 1
                return True
            else:
                print("Enter a valid email adress")
                return False

    def check_password(self):
        if self.flag and not(self.flag_f):
            if len(self.password) < 8 or self.password.isalpha():
                print("Enter a alphanumeric password")
                return False
            if(re.search("[A-Za-z]",self.password) and re.search("[0-9]",self.password) and re.search("[_@$]",self.password)):
                with open("log.txt","a") as f:
                    f.write(self.password+"\n")
                return True

    def check_file(self):
        string = self.email
        file = open("log.txt","r")
        for line in file:
            self.index += 1

            if string in line:
                self.flag_f = 1
                break
        file.close()



#--------------------------------------GRAPHICS-----------------------------------------------------------#

root = Tk()
root.geometry("300x300")
fl = 0

#Declaring String Variable
email_adress = tkinter.StringVar()
password = tkinter.StringVar()

def suggest_password():
    letters = string.ascii_letters+string.digits+string.punctuation
    s = ''.join(random.choice(letters) for i in range(10))
    pass_word = s
    password.set("")
    fl = 1

def submit():
    email = email_adress.get()
    email_adress.set("")
    if fl == 0:
        pass_word = password.get()
        password.set("")

    user = User(email,pass_word)
    user.check_file()
    user.validate_email()
    user.check_password()
    s = suggest_password()
    print(s)

    if user.flag_f == 1:
     messagebox.showinfo("Email","Email already exist")

    print(email,pass_word)



email_label = tkinter.Label(root,text="email", font=('calibre',10, 'bold'))
email_entry = tkinter.Entry(root, textvariable=email_adress, font=('calibre', 10, 'normal'))

passw_label = tkinter.Label(root, text='Password', font=('calibre', 10, 'bold'))
passw_entry = tkinter.Entry(root, textvariable=password, font=('calibre', 10, 'normal'), show='*')


button = tkinter.Button(master=root, text="Sign in", command=submit)
#button1 = tkinter.Button(master=root,text="Suggest Password",command=suggest_password)

email_label.grid(row=1,column=0)
email_entry.grid(row=1,column=1)
passw_label.grid(row=2,column=0)
passw_entry.grid(row=2,column=1)

button.grid(row=4,column=1)
#button1.grid(row=5,column=1)

root.mainloop()


