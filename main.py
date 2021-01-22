import os
from tkinter import filedialog as fd

def del_fig():
    symb = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '+', '.', ' ']

    print("Текущая деректория:", os.getcwd())
    cur_dir = fd.askopenfilename()
    if cur_dir == '':
        cur_dir = os.getcwd()
    os.chdir(cur_dir)
    all_files = os.listdir(cur_dir)

    for th_file in all_files:
        cur_name = th_file
        while len(th_file) >= 5:
            if th_file[0] in symb:
                th_file = th_file[1:]
            else:
                break
        if cur_name != th_file:
            print(f' изменяем: {cur_name} на {th_file}')
            try:
                os.rename(cur_name, th_file)
            except:
                print ('Невозможно поменять файл', cur_name)
    print('done')

def change_name_place():
    print("Текущая деректория:", os.getcwd())
    cur_dir = input('в другой директории:', )
    if cur_dir == '':
        cur_dir = os.getcwd()
    os.chdir(cur_dir)
    all_files = os.listdir(cur_dir)

    for th_file in all_files:
        cur_name = th_file
        while len(th_file) >= 5:
            if th_file [0] in symb:
                th_file = '.idea'
            else:
                break
        if cur_name != th_file:
            print(f' изменяем: {cur_name} на {th_file}')
            try:
                os.rename(cur_name, th_file)
            except:
                print('Невозможно поменять файл', cur_name)
    print('done')



answ = int(input("Удалять цифры спереди - 1, Переставить местами - 2"))
if answ == 1:
    del_fig()