import tkinter 
from tkinter import*
import math

root=Tk()
root.title("Simple calculator")
root.geometry('225x350')
root.resizable(False,False)
root.configure(bg='#17161b')



equation=''
def show(value):
    global equation
    equation=equation +str (value)
    label_result.config(text=equation)

def clear():
    global equation
    equation=''
    c=lambda:clear()
    label_result.config(text=equation)
def equalpress():
     
    try: 
    
     global equation 
     result = str(eval(equation)) 
     label_result.config(text=result) 
     equation = "" 
     
       
    except: 
 
        label_result.config(text=result) 
        equation = "" 

label_result=StringVar()          
label_result =Label(root,width=10,height=3,text="",font=("arial",30))
label_result.pack()

button1=tkinter.Button(root,text='c',width=2,height=1,font=('arial',15,'bold'),bd=1,fg='#fff',bg='#3697f5',command=lambda:clear()).place(x=130,y=300)
button2=tkinter.Button(root,text='+',width=2,height=1,font=('arial',15,'bold'),bd=1,fg='#fff',bg='#3697f5',command=lambda : show('+')).place(x=180,y=150)
button3=tkinter.Button(root,text='-',width=2,height=1,font=('arial',15,'bold'),bd=1,fg='#fff',bg='#3697f5',command=lambda : show('-')).place(x=180,y=200)
button4=tkinter.Button(root,text='*',width=2,height=1,font=('arial',15,'bold'),bd=1,fg='#fff',bg='#3697f5',command=lambda : show('*')).place(x=130,y=200)
button5=tkinter.Button(root,text='/',width=2,height=1,font=('arial',15,'bold'),bd=1,fg='#fff',bg='#3697f5',command=lambda : show('/')).place(x=130,y=150)
button6=tkinter.Button(root,text='9',width=2,height=1,font=('arial',15,'bold'),bd=1,fg='#fff',bg='#3697f5',command=lambda : show('9')).place(x=10,y=150)
button7=tkinter.Button(root,text='8',width=2,height=1,font=('arial',15,'bold'),bd=1,fg='#fff',bg='#3697f5',command=lambda : show('8')).place(x=50,y=150)
button8=tkinter.Button(root,text='7',width=2,height=1,font=('arial',15,'bold'),bd=1,fg='#fff',bg='#3697f5',command=lambda : show('7')).place(x=90,y=150)
button9=tkinter.Button(root,text='6',width=2,height=1,font=('arial',15,'bold'),bd=1,fg='#fff',bg='#3697f5',command=lambda : show('6')).place(x=10,y=200)
button10=tkinter.Button(root,text='5',width=2,height=1,font=('arial',15,'bold'),bd=1,fg='#fff',bg='#3697f5',command=lambda : show('5')).place(x=50,y=200)
button11=tkinter.Button(root,text='4',width=2,height=1,font=('arial',15,'bold'),bd=1,fg='#fff',bg='#3697f5',command=lambda : show('4')).place(x=90,y=200)
button12=tkinter.Button(root,text='3',width=2,height=1,font=('arial',15,'bold'),bd=1,fg='#fff',bg='#3697f5',command=lambda : show('3')).place(x=10,y=250)
button13=tkinter.Button(root,text='2',width=2,height=1,font=('arial',15,'bold'),bd=1,fg='#fff',bg='#3697f5',command=lambda : show('2')).place(x=50,y=250)
button14=tkinter.Button(root,text='1',width=2,height=1,font=('arial',15,'bold'),bd=1,fg='#fff',bg='#3697f5',command=lambda : show('1')).place(x=90,y=250)
button15=tkinter.Button(root,text='0',width=2,height=1,font=('arial',15,'bold'),bd=1,fg='#fff',bg='#3697f5',command=lambda : show('0')).place(x=50,y=300)
button16=tkinter.Button(root,text='.',width=2,height=1,font=('arial',15,'bold'),bd=1,fg='#fff',bg='#3697f5',command=lambda : show('.')).place(x=10,y=300)
button17=tkinter.Button(root,text='=',width=2,height=1,font=('arial',15,'bold'),bd=1,fg='#fff',bg='#3697f5',command= lambda: equalpress() ).place(x=90,y=300)
button18=tkinter.Button(root,text='%',width=2,height=1,font=('arial',15,'bold'),bd=1,fg='#fff',bg='#3697f5',command= lambda : show('%' )).place(x=130,y=250)
button18=tkinter.Button(root,text='(',width=2,height=1,font=('arial',15,'bold'),bd=1,fg='#fff',bg='#3697f5',command= lambda : show('(') ).place(x=180,y=250)
button19=tkinter.Button(root,text=')',width=2,height=1,font=('arial',15,'bold'),bd=1,fg='#fff',bg='#3697f5',command=lambda : show(')') ).place(x=180,y=300)


root.mainloop()






