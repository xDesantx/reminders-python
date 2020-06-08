from notes import Notes as nt
from tkinter import *
'''
#TODO LIST:
learn time
do normal id-based addition
fix 'issue'
#!interface
'''


def show_notes():  # default screen where u see notes

    refresh()

    lb_notes.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky=W+E)


def show_create(): # screen 2 with no loading in list and no delete button

    refresh()


def show_edit(): # screen 2 but with loading the note # !SUCK DIKC
    return 0


def delete_note(): # delete currently editing note
    return 0

def save_note(): # apply changes to note
    return 0

def refresh():  # refresh list of notes load/add/edit/delete
    global lb_notes

    nots = notes_.get_notes()

    lb_notes.delete(0, END)
    for i in nots:
        lb_notes.insert(END, i)

# TODO learn time


def add_():  # create new note test!!!
    notes_.addNew('some test text', 'time i cant use it lmao')  # add note
    refresh()


if __name__ == '__main__':  # main

    root = Tk()  # opentk
    root.geometry('600x600')
    root.title('hah text t')

    # 1st screen
    lb_notes = Listbox(width=590, height=500)
    btn_new = Button(text='new note', command=show_create, width=190, height=90,)
    btn_view = Button(text='view', command=show_edit, width=190, height=90,)
    # 2nd screen
    txt_text = Text(width=590,height=400)
    btn_save=Button(text='save',width=190, height=90, command=save_note)
    btn_cancel=Button(text='cancel',width=190, height=90, command=show_notes)
    btn_delete=Button(text='delete',width=190, height=90 ,command=delete_note)
    ent_datetime=Entry(width=590)

    notes_ = nt()

    show_notes()
    root.mainloop()
    del notes_
