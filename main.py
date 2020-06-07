from notes import Notes as nt
from tkinter import *

def placeElements():
    global notes_lb
    
    notes_lb.grid(row=0, column=0, columnspan=3)
    Button(text='add',command=add_).grid(row=1, column=0)

def refresh():
    nots=notes_.get_notes()
    
    notes_lb.delete(0,-1)
    for i in nots:
        notes_lb.insert(-1, i)

def add_(): #TODO learn time
    notes_.addNew('some test text', 'time i cant use it lmao')
    refresh()

if __name__=='__main__':
    global notes_
    global notes_lb

    root=Tk()
    root.geometry('600x600')
    root.title('hah text t')

    notes_lb=Listbox()
    notes_=nt()

    placeElements()
    root.mainloop()