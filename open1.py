from csv import *

def open_book1():

    with open('0002.txt', 'w', encoding='utf_8') as f:
        f.seek(0)

    with open("0001.txt", 'r', encoding='utf_8') as f:
        for line in f:
            text = line.split('stk')
            with open('0002.txt', 'a', encoding='utf_8') as data:
                data.write("{d1}____________________{d2}\n".format(d1=text[0], d2=text[1]))


def open_book2():

    with open('0002.csv', 'w', encoding='utf_8') as f:
        f.seek(0)

    with open("0001.csv", 'r', encoding='utf_8') as f:
        for line in f:
            text = line.split('stk')
            with open('0002.csv', 'a', encoding='utf_8') as data:
                data.write("{d1}____________________{d2}\n".format(d1=text[0], d2=text[1]))


def convert_1():
    with open('0001.txt', 'r', encoding='utf_8') as code:
        code = code.read()
    with open('0001.csv', 'w', encoding='utf_8') as cod:
        cod.write(code)


def convert_2():
    with open('0001.csv', 'r', encoding='utf_8') as code:
        code = code.read()
    with open('0001.txt', 'w', encoding='utf_8') as cod:
        cod.write(code)