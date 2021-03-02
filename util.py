import os

def del_fig():
# убирает цифры и символы спереди у названия файла
    symb = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '+', '.', ' ']

    print("Текущая директория:", os.getcwd())
    cur_dir = str(input("Введите новую директорию: "))
#   cur_dir = fd.askopenfilename()
    if cur_dir == '':
        cur_dir = os.getcwd()
    os.chdir(cur_dir)
    all_files = os.listdir(cur_dir)
    logfile = open('logfile.txt', 'w', encoding='utf-8')
    for th_file in all_files:
        if checkfilemp3(th_file):
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
                    print(f'{cur_name} ; {th_file}', file=logfile)
                except:
                    print ('Невозможно поменять файл', cur_name)
    print('done')
    logfile.close()


def checkfilemp3 (checkfile):
# проверяет расширение на mp3
    if checkfile.count('.mp3') > 0:
        return True
    else:
        return False


def change_name_place():
# меняет местами исполнителя и название
    print("Текущая директория:", os.getcwd())
    cur_dir = str(input("Введите новую директорию: "))
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

def capitalize_name():
# первые буквы большие - остальные маленькие
    print("Текущая директория:", os.getcwd())
    cur_dir = str(input("Введите новую директорию: "))
    #   cur_dir = fd.askopenfilename()
    if cur_dir == '':
        cur_dir = os.getcwd()
    os.chdir(cur_dir)
    all_files = os.listdir(cur_dir)
    logfile = open('logfile.txt', 'w', encoding='utf-8')
    for th_file in all_files:
        if checkfilemp3(th_file):
            cur_name = th_file
            if th_file.count('-') > 0:
                chnamelist = th_file.split('-')
                for i in range(len(chnamelist)):
                    chnamelist[i] = chnamelist[i].strip().capitalize()
                th_file = ' - '.join(chnamelist)
            else:
                th_file = th_file.capitalize()

            if cur_name != th_file:
                print(f' изменяем: {cur_name} на {th_file}')

                try:
                    os.rename(cur_name, th_file)
                    print(f'{cur_name} ; {th_file}', file=logfile)
                except:
                    print('Невозможно поменять файл', cur_name)
    print('done')
    logfile.close()