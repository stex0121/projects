import tkinter 
from tkinter import*
from tkinter import filedialog


root=Tk()
root.geometry('500x600')
root.title('Python notepad')
root.config(bg='lightblue')
root.resizable(False,False)


def Save_file():
    
    Open_file=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    if Open_file is None:
        return
    Text=str(Entry.get(1.0,END))
    Open_file.write(Text)
    Open_file.close()

def Open_file():
    print('')
    file=filedialog.askopenfile(mode='r',filetype=[('text files','*.txt')])
    if file is not None:
        content=file.read()
        Entry.insert(INSERT,content)
    
def exit():
    root.destroy()


b1=Button(root,width=8,height=2,bg='#fff',text='Save file',command=Save_file).place(x=200,y=4)
b2=Button(root,width=8,height=2,bg="#fff",text='Open file',command=Open_file).place(x=100,y=4)
b3=Button(root,width=8,height=2,bg="#fff",text='Exit',command=exit).place(x=300,y=4)
Entry=Text(root,width='59',height='30',bg='white',wrap=WORD)
Entry.place(x=12,y=50)


root.mainloop()
