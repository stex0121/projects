import tkinter
from tkinter import *



root=Tk()
root.title=('Add to do list')
root.geometry('450x550+400+100')
root.resizable(False,False)
root.configure(bg='pink')

task_list=[]

def openTaskfile():
    
   try:
       global task_list
       with open('tasklist.txt' ,'r') as taskfile:
        tasks=taskfile.readlines()
        for task in  tasks:
          if task !='\n':
             task_list.append(task)
             listbox.insert(END,task)
   except:
      file=open('tasklist.txt','w')
      file.close()

def addtask():
   task=task_entry.get()
   task_entry.delete(0,END)
   if task:
      with open('tasklist.txt','a') as taskfile:
         taskfile.write(f'\n{task}')
         task_list.append(task)
         listbox.insert(END,task)

Topimage=PhotoImage(file='topbar.png')
Label(root,image=Topimage).place(x=100,y=20)

def delete():
   global task_list
   task=str(listbox.get(ANCHOR))
   if task in task_list:
      task_list.remove(task)
      with open ('tasklist.txt','w') as taskfile:
         for task in task_list:
            taskfile.write(task +'\n')
            
      listbox.delete(ANCHOR)







frame=Frame(root,width=350,height=30,bg='white')
frame.place(x=50,y=100)

task=StringVar
task_entry=Entry(frame,width=18,font='arial 20',bd=0)
task_entry.place(x=10,y=0)
task_entry.focus()
button=Button(frame,text='ADD',font='arial 14 bold',width=8,bd=0,bg="#5a95ff",fg="#fff",command=addtask)
button.place(x=250,y=0)

frame1=Frame(root,bd=3,width=400,height=400,bg='#32405b')
frame1.pack(pady=(160,0))
listbox=Listbox(frame1,width=40,height=16,bg='#32405b',font='arial 12 bold',fg='white',cursor='hand2',selectbackground='#5a95ff')
listbox.pack(side=LEFT,fill=BOTH,padx=2)
scroolbar=Scrollbar(frame1)
scroolbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scroolbar.set)
scroolbar.config(command=listbox.yview)



delete_icon=PhotoImage(file='delete.png')
Button(root,image=delete_icon,bd=0,command=delete).pack(side=BOTTOM,pady=13)

openTaskfile()

root.mainloop()

