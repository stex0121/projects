
from tkinter import*

root=Tk()
root.geometry('450x250+200+100')
root.resizable(False,False)

def from_kg():
    gram=float(label1_value.get())*1000
    pound=float(label1_value.get())*2.20462
    ounce=float(label1_value.get())*35.274
    text1.delete('1.0',END)
    text1.insert(END,gram)
    text2.delete('1.0',END)
    text2.insert(END,pound)
    text3.delete('1.0',END)
    text3.insert(END,ounce)
label1_value=StringVar()
label1=Label(root,text='Enter the weight in Kg:')
label1.place(x=0,y=50)
label1=Entry(root,textvariable=label1_value)
label1.place(x=122,y=50)
label2=Label(root,text='Gram:')
label2.place(x=0,y=100)
label3=Label(root,text='Pounds:')
label3.place(x=125,y=100)
label4=Label(root,text='Ounce:')
label4.place(x=250,y=100)
text1=Text(root,height=1,width=8)
text1.place(x=50,y=100)
text2=Text(root,height=1,width=8)
text2.place(x=180,y=100)
text3=Text(root,height=1,width=8)
text3.place(x=300,y=100)

button1=Button(root,text='Convert',command=from_kg)
button1.place(x=100,y=200)
root.mainloop()