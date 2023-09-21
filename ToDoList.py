from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("Error", "You have to add some task.")

def deleteTask():
    lb.delete(ANCHOR)
    
ws = Tk()
ws.config(bg='light pink')
ws.geometry('500x950+800+100')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=10)




task_list = [
    '👉play cricket',
    '👉read a book',
    '👉watch a movie',
    '👉sing a song',
    '👉go to gym',
    '👉take a bath',
    '👉paly with friends',
    '👉take a selfi'
    ]

lb = Listbox(
    frame,
    width=25,
    height=15,
    font=('Times', 18),
    bd=0,
    fg='black',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('times', 24)
    )

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
   
     bg='yellow',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


ws.mainloop()