from tkinter import *
from open1 import *
from csv import *

def all_cont_txt():
    
    def click(event):
        root.destroy()

    open_book1()

    with open("0002.txt", 'r', encoding='utf_8') as f:
        name = f.read()

    root = Tk()
    root.title('Все контакты (.txt)')
    root.minsize(width=500, height=400)

    but = Button(root, text='Выход',
                width=20, height=2, bg='white', fg='blue',bd=3)


    lab_name = Label(root, text=name , font="Arial 10", width=60)

    but.grid(row=0, column=0)
    lab_name.grid(row=1, column=0)

    but.bind("<Button-1>", click)


    root.mainloop()




def all_cont_csv():
    
    def click(event):
        root.destroy()

    open_book2()

    with open("0002.csv", 'r', encoding='utf_8') as f:
        name = f.read()

    root = Tk()
    root.title('Все контакты (.csv)')
    root.minsize(width=500, height=400)

    but = Button(root, text='Выход',
                width=20, height=2, bg='white', fg='blue',bd=3)


    lab_name = Label(root, text=name , font="Arial 10", width=60)

    but.grid(row=0, column=0)
    lab_name.grid(row=1, column=0)

    but.bind("<Button-1>", click)


    root.mainloop()

