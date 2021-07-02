import tkinter
import pickle
from tkinter import messagebox
from tkinter import*
root = Tk()
root.title("DO TO LIST APP")
root.geometry("1000x600+0+0")
root.config(bg="purple")
def add_task():
    task = entrybox.get()
    if task!="":
        listbox.insert(END,task)
        entrybox.delete(0,END)
    else:
        messagebox.showwarning(title="Warning",message="YOU MUST ENTER TASK")

def delete_task():
    try:
        task_index = listbox.curselection()[0]
        listbox.delete(task_index)
    except:
        messagebox.showwarning(title="Warning",message="YOU MUST SELECT TASK ")

def save_task():
    tasks = listbox.get(0,listbox.size())
    pickle.dump(tasks,open("task.dat","wb"))
    listbox.delete(0,END)

def load_task():
    try:
        task1= pickle.load(open("task.dat","rb"))
        listbox.delete(0,END)
        for tas in task1:
            listbox.insert(END,tas)
    except:
        messagebox.showwarning(title="Warning",message="FILE DOES NOT FOUND")

label1 = Label(root,text="TO DO LIST APP",font=("bold"),fg="black")
label1.place(x=500,y=0)
frame1 = Frame(root)
frame1.pack()
frame1.config(bg="pink")
listbox = Listbox(frame1,height=20,width=100,bd=10)
listbox.pack(side=LEFT)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill= Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
entrybox = Entry(root,width=100,bd=10)
entrybox.place(x=90,y=400)
add_button1 = Button(root,bd=10,text="Add Data",bg="black",fg="white",relief=SUNKEN,command=add_task)
add_button1.place(x=90,y=450)
delete_button1 = Button(root,bd=10,text="Delete Data",bg="black",fg="white",relief=SUNKEN,command=delete_task)
delete_button1.place(x=250,y=450)
save_button1 = Button(root,bd=10,text="Save Data",bg="black",fg="white",relief=SUNKEN,command=save_task)
save_button1.place(x=410,y=450)
load_button1 = Button(root,bd=10,text="Load Data",bg="black",fg="white",relief=SUNKEN,command=load_task)
load_button1.place(x=570,y=450)
clear_button1 = Button(root,bd=10,text="Exit ",bg="black",fg="white",relief=SUNKEN,command=root.destroy)
clear_button1.place(x=710,y=450)



root.mainloop()