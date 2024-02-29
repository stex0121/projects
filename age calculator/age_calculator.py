import tkinter
from tkinter import *
import random 
from datetime import date

root=Tk()
root.geometry('800x600')
root.resizable(False,False)
root.title('Age calculator')
root.configure(bg='#808080')

def Calculate_age():
 today=date.today()
 birthdate=date(int(yearentry.get()),int(monthentry.get()),int(dayentry.get()))
 age=(today.year - birthdate.year -1 )
 Label(text=f'{nameentry.get()} youre age is {age}',font='30').place(x=300,y=480)


photo=PhotoImage(file='tempsnip.png')
myimage=Label(image=photo)
myimage.pack(padx=15,pady=10)

Label(text='Name',font=20).place(x=200,y=300)
Label(text='Year',font=20).place(x=200,y=350)
Label(text='Month',font=20).place(x=200,y=400)
Label(text='Day',font=20).place(x=200,y=450)

NameValue=StringVar()
YearValue=StringVar()
MonthValue=StringVar()
DayValue=StringVar()

nameentry=Entry(root,textvariable=NameValue,font=20,width=30,bd=3)
nameentry.place(x=300,y=300)


yearentry=Entry(root,textvariable=YearValue,font=20,width=30,bd=3)
yearentry.place(x=300,y=350)

monthentry=Entry(root,textvariable=MonthValue,font=20,width=30,bd=3)
monthentry.place(x=300,y=400)

dayentry=Entry(root,textvariable=DayValue,font=20,width=30,bd=3)
dayentry.place(x=300,y=450)

Button(text='calculate age',font='20',bg='white',fg='black',width=11,height=2,command=Calculate_age).place(x=300,y=500)

root.mainloop()



    

