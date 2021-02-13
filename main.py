import os
from util import *
from tkinter import filedialog as fd



def change_name_place():
# меняет местами исполнителя и название
    print("Текущая директория:", os.getcwd())
    cur_dir = str(input())
    #   cur_dir = fd.askopenfilename()
    if cur_dir == '':
        cur_dir = os.getcwd()
    os.chdir(cur_dir)
    all_files = os.listdir(cur_dir)
    logfile = open('logfile.txt', 'w', encoding='utf-8')
    for th_file in all_files:
        if checkfilemp3(th_file):
            cur_name = th_file
            if th_file.count(' - ') > 0:
                th_file = th_file[0: -4]
                chnamelist = th_file.split(' - ')
                th_file = chnamelist[1] + ' - ' + chnamelist[0] + '.mp3'

            if cur_name != th_file:
                print(f' изменяем: {cur_name} на {th_file}')

                try:
                    os.rename(cur_name, th_file)
                    print(f'{cur_name} ; {th_file}', file=logfile)
                except:
                    print('Невозможно поменять файл', cur_name)
    print('done')
    logfile.close()




answ = int(input("Удалять цифры спереди - 1, Переставить местами - 2: "))
if answ == 1:
    del_fig()
elif answ == 2:
    change_name_place()
