from tkinter import *
from add_contact import *
from all_contact import *


def main_tk():

    def click(event):
        add_cont()

    def click2(event):
        all_cont_txt()

    def click3(event):
        add_cont_2()

    def click4(event):
        all_cont_csv()

    def click5(event):
        root.destroy()


    root = Tk()
    root.title('Телефонный справочник.')
    root.minsize(width=500, height=200)

    but = Button(root, text='Добавить контакт\n в file.txt',
                width=20, height=2, bg='white', fg='blue',bd=3)

    but1 = Button(root, text='Показать все контакты\n в file.txt',
                width=20, height=2, bg='white', fg='blue',bd=3)

    but2 = Button(root, text='Добавить контакт\n в file.csv',
                width=20, height=2, bg='white', fg='blue',bd=3)

    but3 = Button(root, text='Показать все контакты\n в file.csv',
                width=20, height=2, bg='white', fg='blue',bd=3)

    but4 = Button(root, text='Выход', font="Arial 12",
                width=15, height=3, bg='white', fg='blue',bd=5)




    but.grid(row=0, column=0)
    but1.grid(row=1, column=0)
    but2.grid(row=0, column=2)
    but3.grid(row=1, column=2)
    but4.grid(row=2, column=1)


    but.bind("<Button-1>", click)
    but1.bind("<Button-1>", click2)
    but2.bind("<Button-1>", click3)
    but3.bind("<Button-1>", click4)
    but4.bind("<Button-1>", click5)


    root.mainloop()