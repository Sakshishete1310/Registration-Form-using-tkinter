from tkinter import *
from tkinter import messagebox
screen=Tk()
screen.title("Registration Form")
screen.geometry("400x400")
screen.resizable(False,False)
def register():
    name=name_info.get()
    age=age_info.get()
    phone=phone_info.get()
    email=email_info.get()
    if name=="":
       messagebox.showerror("Error","please enter your name")

    elif age=="":
       messagebox.showerror("Error","please enter your age")

    elif phone=="":
       messagebox.showerror("Error","please enter your phone no")

    elif email=="":
       messagebox.showerror("Error","please enter your email id")                        
    else:
       Label(screen,text="Registration Sucessfull",font="20",fg="pink").place(x=135,y=285)

    with open(name+".txt","w")as f:
     f.write("name: "+name+"\n")
     f.write("age: "+age+"\n")
     f.write("phone number: "+phone+"\n")
     f.write("email: "+email+"\n")
        
Label(screen,text="Registration Form",font="ariel 20 bold",bg="blue",fg="white").pack(fill="both")

Label(screen,text="Name",font="20").place(x=40,y=75)
Label(screen,text="Age",font="20").place(x=40,y=115)
Label(screen,text="Phone No",font="20").place(x=40,y=155)
Label(screen,text="Email Id",font="20").place(x=40,y=195)

name_info=StringVar()
age_info=StringVar()
phone_info=StringVar()
email_info=StringVar()

name_entry=Entry(screen,font="10",bd=4,textvariable=name_info)
name_entry.place(x=140,y=75)

age_entry=Entry(screen,font="10",bd=4,textvariable=age_info)
age_entry.place(x=140,y=115)

phone_entry=Entry(screen,font="10",bd=4,textvariable=phone_info)
phone_entry.place(x=140,y=155)

email_entry=Entry(screen,font="10",bd=4,textvariable=email_info)
email_entry.place(x=140,y=195)

Button(screen,text="Register",font="20",command=register).place(x=185,y=255)
mainloop()
