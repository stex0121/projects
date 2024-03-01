from tkinter import*
from tkinter import messagebox
import ast

root=Tk()
root.title('Sign up')
root.geometry('925x500+300+200')
root.resizable(False,False)
root.config(bg='#fff')

def sign_in():
    root.destroy()
    import Sing_in




image=PhotoImage(file='sign_up.png')
Label(root,image=image,border=0,bg='white').place(x=20,y=-10)

frame=Frame(root,width=350,height=390,bg='#fff')
frame.place(x=480,y=50)

heading=Label(frame,text='Sign up',font='Arial 15 bold',bd=0,bg='white',fg='#57a1f8')
heading.place(x=100,y=5)

def on_enter(e):
    user.delete('0',END)

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert=('0','Username : ')


user=Entry(frame,width=25,fg='black',bg='white',bd=0,font='arila 11 bold')
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

def on_enter(e):
    password.delete('0',END)

def on_leave(e):
    name=password.get()
    if name=='':
        password.insert=('0','password : ')

password=Entry(frame,width=25,fg='black',bg='white',bd=0,font='arila 11 bold')
password.place(x=30,y=150)
password.insert(0,'Password')
password.bind('<FocusIn>',on_enter)
password.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)


Button(frame,width=39,pady=7,text='Sign up',bg='#57a1f8',fg='white',bd=0).place(x=35,y=280)
label=Label(frame,text='I have an account',fg='black',bg='white',font='arial 9')
label.place(x=90,y=340)

signin=Button(frame,width=6,text='Sign in',bd=0,bg='white',cursor='hand2',fg='#57a1f8',command=sign_in)
signin.place(x=200,y=340)

root.mainloop()


