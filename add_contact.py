from tkinter import *
from open1 import *
from csv import *


def add_cont():    

    def click(event):
        res = ent_name.get()
        res1 = ent_num.get()
        with open("0001.txt", 'a', encoding='utf_8') as f:
            f.write((f"{res}")+'stk'+(f"{res1}\n"))
        convert_1()
        root.destroy()

            
    root = Tk()
    root.title('Добавить контакт (.txt)')
    root.minsize(width=550, height=140)


    lbl_name = Label(root, text='Введите имя контакта', width=30)
    lbl_num = Label(root, text='Введите номер телефона', width=30)

    ent_name = Entry(root, width=30, font="Arial 12", state='normal', bd=5)
    ent_num = Entry(root, width=30, font="Arial 12", state='normal', bd=5)



    but = Button(root, text='Добавить контакт',
                width=20, height=2, bg='white', fg='blue',bd=3)

    lbl_name.grid(row=0, column=0)
    lbl_num.grid(row=1, column=0)

    ent_name.grid(row=0, column=1)
    ent_num.grid(row=1, column=1)
    but.grid(row=2, column=1)


    but.bind("<Button-1>", click)

    root.mainloop()




def add_cont_2():    

    def click(event):
        res = ent_name.get()
        res1 = ent_num.get()
        with open("0001.csv", 'a', encoding='utf_8') as f:
            f.write((f"{res}")+'stk'+(f"{res1}\n"))
        convert_2()
        root.destroy()

            
    root = Tk()
    root.title('Добавить контакт (.csv)')
    root.minsize(width=550, height=140)


    lbl_name = Label(root, text='Введите имя контакта', width=30)
    lbl_num = Label(root, text='Введите номер телефона', width=30)

    ent_name = Entry(root, width=30, font="Arial 12", state='normal', bd=5)
    ent_num = Entry(root, width=30, font="Arial 12", state='normal', bd=5)



    but = Button(root, text='Добавить контакт',
                width=20, height=2, bg='white', fg='blue',bd=3)

    lbl_name.grid(row=0, column=0)
    lbl_num.grid(row=1, column=0)

    ent_name.grid(row=0, column=1)
    ent_num.grid(row=1, column=1)
    but.grid(row=2, column=1)


    but.bind("<Button-1>", click)

    root.mainloop()