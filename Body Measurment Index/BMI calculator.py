from tkinter import *
import tkinter as tk
from PIL import Image , ImageTk
from tkinter import ttk

root=Tk()
root.title('BMI CALCULATOR')
root.geometry('470x600+300+200')
root.resizable(False,False)
root.config(bg='#f0f1f5')


def BMI():

    h=float(height.get())
    w=float(weight.get())
    m=h/100
    bmi=round((w/m**2),1)
    print(bmi)
    Label1.config(text=bmi)
    if bmi<18.5:
        Label2.config(text='Underweight')
        Label3.config(text='You have lower weight then normal body!')
    elif bmi>18.5:
        Label2.config(text='Normal')
        Label3.config(text='It indicates that you are healthy!')
    elif bmi>25 and bmi<30:
        Label2.config(text='Overweight')
        Label3.config(text='You have more weight then normal body!')
    else :
        Label2.config(text='Obessity')
        Label3.config(text='Youre Health is in risk of obessity!') 

image_icon=PhotoImage(file='icon.png')
root.iconphoto(False,image_icon)

top=PhotoImage(file='top.png')
top_image=Label(root,image=top,background='#f0f1f5')
top_image.place(x=-10,y=-10)


Label(root,width=72,height=19,bg='lightblue').pack(side=BOTTOM)

box=PhotoImage(file='box.png')
Label(root,image=box).place(x=20,y=100)
Label(root,image=box).place(x=240,y=100)


scale=PhotoImage(file='scale.png')
Label(root,image=scale,bg='lightblue').place(x=20,y=310)


current_value=tk.DoubleVar()
def get_current_value():
    return '{: .2f}'.format(current_value.get())
def slider_change(event):
    height.set(get_current_value())

    size=int(float(get_current_value()))
    img=(Image.open('man.png'))
    resized_image=img.resize((50,10+size))
    photo2=ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=70,y=550-size)
    secondimage.image=photo2

style=ttk.Style()
style.configure('TScale',background='red')
slider=ttk.Scale(root,from_=0, to=220,orient='horizontal',style='TScale',command=slider_change,variable=current_value)
slider.place(x=80,y=250)

current_value2=tk.DoubleVar()
def get_current_value2():
    return '{: .2f}'.format(current_value2.get())
def slider_change2(event):
    weight.set(get_current_value2())

style2=ttk.Style()
style2.configure('TScale',background='red')
slider2=ttk.Scale(root,from_=0, to=200,orient='horizontal',style='TScale',command=slider_change2,variable=current_value2)
slider2.place(x=300,y=250)




height=StringVar()
weight=StringVar()

height_entry=Entry(root,textvariable=height,bg='#f0f1f5',bd=0,width=5,fg='#000000',font='arial 50',justify=CENTER)
height_entry.place(x=35,y=160)
height.set(get_current_value())

weight_entry=Entry(root,textvariable=weight,bg='#f0f1f5',bd=0,width=5,fg='#000000',font='arial 50',justify=CENTER)
weight_entry.place(x=255,y=160)
weight.set(get_current_value2())

secondimage=Label(root,bg='lightblue')
secondimage.place(x=70,y=530)

Button(root,text='View Report',width=15,height=2,font='arial 10 bold',bg='#1f6e68',fg='white',command=BMI).place(x=280,y=340)

Label1=Label(root,font='arial 20 bold',bg='lightblue',fg='#fff')
Label1.place(x=125,y=305)

Label2=Label(root,font='arial 20 bold',bg='lightblue',fg='#3b3a3a')
Label2.place(x=280,y=430)

Label3=Label(root,font='arial 10 bold',bg='lightblue',)
Label3.place(x=200,y=500)



root.mainloop()