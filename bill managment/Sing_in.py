import tkinter
from tkinter import *
from tkinter import messagebox
root=Tk()
root.title('Login')
root.geometry('600x300')
root.resizable(False,False)


def sing_in():
    Username=user.get()
    Password=code.get()

    if Username=='admin' and Password=='1234':
       print('Stefan Mihajlovic')
    elif Username != 'admin' and Password!='1234':
        messagebox.showerror('Invalid','Invalid Username or Passowrd')
    elif Password !='1234':
        messagebox.showerror("Invalid",'Invalid Password')
    elif Username !='1234':
        messagebox.showerror("Invalid",'Invalid Username')
    root.destroy()


img=PhotoImage(file='log_in.png')
Label(root,image=img,bg='black').place(x=0,y=0)

frame=Frame(root,width=300,height=300,bg='white')
frame.place(x=300,y=0)

heading=Label(frame,text='Log in',bg='white',fg='blue',font='arial,15')
heading.place(x=100,y=5)

    

def on_enter(e):
    user.delete('0',END)

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert=('0','Username : ')


user=Entry(frame,width=25,border=2,bg='white',font='arial,10')
user.place(x=10,y=80)
user.insert(0,'Username : ')
user.bind('<FocusIn>',on_enter)
user.bind("<FocusOut>",on_leave)

def on_enter(e):
    code.delete('0',END)

def on_leave(e):
    name=code.get()
    if name=='':
        user.insert=('0','Password : ')


code=Entry(frame,width=25,border=2,bg='white',font='arial,10')
code.place(x=10,y=150)
code.insert(0,'Password : ')
code.bind('<FocusIn>',on_enter)
code.bind("<FocusOut>",on_leave)





sing_in=Button(frame,width=30,height=2,text='Log in',border=2,bg='blue',fg='white',command=sing_in)
sing_in.place(x=20,y=200)


root.mainloop()