from tkinter import *
import Sing_in

root=Tk()
root.geometry('1000x500')
root.title('Bill Managment')
root.resizable(False,False)

def reset():
    entry_coffe.delete(0,END)
    entry_tea.delete(0,END)
    entry_beer.delete(0,END)
    entry_juice.delete(0,END)
    entry_kebab_doner.delete(0,END)
    entry_plasmashake.delete(0,END)
    entry_sandwich.delete(0,END)

def total():
    try:a1=int(coffe.get())
    except: a1=0

    try:a2=int(tea.get())
    except: a2=0

    try:a3=int(beer.get())
    except: a3=0

    try:a4=int(juice.get())
    except: a4=0

    try:a5=int(kebab_doner.get())
    except: a5=0

    try:a6=int(plasmashake.get())
    except: a6=0

    try:a7=int(sandwich.get())
    except: a7=0

    c1=120*a1
    c2=60*a2
    c3=150*a3
    c4=200*a4
    c5=400*a5
    c6=300*a6
    c7=300*a7

    lbl_total=Label(f2,font=('arial,20,bold'),text='total',width=16,fg='black',)
    lbl_total.place(x=50,y=50)
    entry_total=Entry(f2,font='arial,20,bold',textvariable=total_bill,bd=6,width=15,bg='lightgreen')
    entry_total.place(x=50,y=100)

    total_cost=c1+c2+c3+c4+c5+c6+c7
    string_bill='Rsd.',float('% 2f' %total_cost)
    total_bill.set(string_bill)

Label(text='Bill managmeent',width=300,height=2,font='calibri 33',bg='black',fg='white').pack()

f=Frame(root,width=300,highlightbackground='black',highlightthickness='1',height=370,bg='lightblue')
f.place(x=10,y=118)

Label(f,text='Menu',font='Gabriola 40 bold',fg='black',bg='lightblue').place(x=80,y=0)
Label(f,text='coffe.......120.Rsd/cup',fg='black',bg='lightblue').place(x=10,y=80)
Label(f,text='tea.......60.Rsd/cup',fg='black',bg='lightblue').place(x=10,y=100)
Label(f,text='juice.......200.Rsd/cup',fg='black',bg='lightblue').place(x=10,y=120)
Label(f,text='plasma shake.......300.Rsd/cup',fg='black',bg='lightblue').place(x=10,y=140)
Label(f,text='beer.......150.Rsd/cup',fg='black',bg='lightblue').place(x=10,y=160)
Label(f,text='kebab doner.......400.Rsd/plate',fg='black',bg='lightblue').place(x=10,y=180)
Label(f,text='sandwich.......300.Rsd/plate',fg='black',bg='lightblue').place(x=10,y=200)
f2=Frame(root,bg='lightyellow',highlightbackground='black',highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)
Bill=Label(f2,text='Bill',font='arial,20,bold',bg='lightyellow')
Bill.place(x=120,y=10)

f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

coffe=StringVar()
tea=StringVar()
juice=StringVar()
plasmashake=StringVar()
beer=StringVar()
kebab_doner=StringVar()
sandwich=StringVar()
total_bill=StringVar()

lbl_coffe=Label(f1,font=('aria',20,'bold'),text='coffe',width=12,fg='red')
lbl_tea=Label(f1,font=('aria',20,'bold'),text='tea',width=12,fg='red')
lbl_juice=Label(f1,font=('aria',20,'bold'),text='juice',width=12,fg='red')
lbl_plasmashake=Label(f1,font=('aria',20,'bold'),text='plasmashake',width=12,fg='red')
lbl_beer=Label(f1,font=('aria',20,'bold'),text='beer',width=12,fg='red')
lbl_kebab_doner=Label(f1,font=('aria',20,'bold'),text='kebabdoner',width=12,fg='red')
lbl_sandwich=Label(f1,font=('aria',20,'bold'),text='sandwich',width=12,fg='red')
lbl_coffe.grid(row=1,column=0)
lbl_tea.grid(row=2,column=0)
lbl_juice.grid(row=3,column=0)
lbl_plasmashake.grid(row=4,column=0)
lbl_beer.grid(row=5,column=0)
lbl_kebab_doner.grid(row=6,column=0)
lbl_sandwich.grid(row=7,column=0)

entry_coffe=Entry(f1,font=('arial',20,'bold'),textvariable=coffe,bd=6,width=8,bg='lightpink')
entry_tea=Entry(f1,font=('arial',20,'bold'),textvariable=tea,bd=6,width=8,bg='lightpink')
entry_juice=Entry(f1,font=('arial',20,'bold'),textvariable=juice,bd=6,width=8,bg='lightpink')
entry_plasmashake=Entry(f1,font=('arial',20,'bold'),textvariable=plasmashake,bd=6,width=8,bg='lightpink')
entry_beer=Entry(f1,font=('arial',20,'bold'),textvariable=beer,bd=6,width=8,bg='lightpink')
entry_sandwich=Entry(f1,font=('arial',20,'bold'),textvariable=sandwich,bd=6,width=8,bg='lightpink')
entry_kebab_doner=Entry(f1,font=('arial',20,'bold'),textvariable=kebab_doner,bd=6,width=8,bg='lightpink')
entry_coffe.grid(row=1,column=1)
entry_tea.grid(row=2,column=1)
entry_juice.grid(row=3,column=1)
entry_plasmashake.grid(row=4,column=1)
entry_beer.grid(row=5,column=1)
entry_kebab_doner.grid(row=6,column=1)
entry_sandwich.grid(row=7,column=1)

btn_reset=Button(f1,bd=5,fg='black',bg='lightblue',font='arial 15 bold',width=10,text='reset',command=reset)
btn_reset.grid(row=8,column=0)
btn_total=Button(f1,bd=5,fg='black',bg='lightblue',font='arial,16,bold',width=10,text='total',command=total)
btn_total.grid(row=8,column=1)

root.mainloop()

