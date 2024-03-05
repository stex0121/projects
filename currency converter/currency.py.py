from tkinter import *

root=Tk()
root.geometry('320x500')
root.title('currency converter')
root.configure(bg='#808080')

def convert():
    cn1.delete(0,END)
    value=int(cn.get())
    value_1=value * 117.17
    value_2=value * 107,84
    cn1.insert(0,str(value_1))
    cn2.insert(0,str(value_2))

   
   
label = Label(root,text="Currency Converter",relief="raised",borderwidth=2,font= ('arial',25),bg='#fff',padx=20,pady=10)
label.pack(padx=10,pady=10)
label1 =Label(root,text="EUR",font= ('arial',25),bg='#fff')
label1.pack(padx=2,pady=2)
label1 =Label(root,text="USD",font= ('arial',25),bg='#fff')
label1.pack(padx=2,pady=2)
cn = Entry(root,highlightthickness=1, width=30)
cn.pack(padx=2,pady=2)
buttton = Button(root,text="TO",command=convert,width=10)
buttton.pack(padx=2,pady=2)
label2=Label(root,text="RSD",font= ('arial',25),bg='#fff')
label2.pack(padx=2,pady=2)
cn1=Entry(root,highlightthickness=1, width=30)
cn1.pack(padx=2,pady=2)
cn2=Entry(root,highlightthickness=1, width=30)
cn2.pack(padx=2,pady=2)

root.mainloop()