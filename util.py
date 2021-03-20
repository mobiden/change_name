import os

def start(cur_dir, rec):
    print("Удалять цифры спереди - 1 \n" 
                     "Переставить местами - 2 \n"
                     "Все буквы, кроме первой строчные - 3\n"
                    "Добавить исполнителя спереди - 4\n"
                    'Поменять латинские буквы на русские - 5'
          )
    answ = int(input("Номер? "))
    if answ == 1:
        del_fig(cur_dir,rec)
    elif answ == 2:
        change_name_place(cur_dir, rec)
    elif answ == 3:
        capitalize_name(cur_dir, rec)
    elif answ == 4:
        add_artists(cur_dir, rec)
    elif answ == 5:
        latin_to_rus(cur_dir, rec)
    elif answ == 6:
        unchanging(cur_dir)
def end_of_def(cur_dir):
    ans = input('Продолжаем? ')
    if ans == 'y' or ans == 'Y' or ans =


def record_of_change(cur_name, th_file, logfile):
    if cur_name != th_file:
        print(f' изменяем: {cur_name} на {th_file}')

        try:
            os.rename(cur_name, th_file)
            print(f'{cur_name} ;;; {th_file}', file=logfile)
        except:
            print('Невозможно поменять файл', cur_name)

def curr_dir():
# запрос директории
    print("Текущая директория:", os.getcwd())
    cur_dir = str(input("Введите новую директорию: "))
    #   cur_dir = fd.askopenfilename()
    if cur_dir == '':
        cur_dir = os.getcwd()
    os.chdir(cur_dir)
    return cur_dir

def checkfilemp3 (checkfile):
# проверяет расширение на mp3
    return checkfile.lower().count('.mp3') > 0

def del_fig(cur_dir,rec):
# убирает цифры и символы спереди у названия файла
    symb = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '+', '.', ' ']
    if cur_dir == '':
        cur_dir = curr_dir()
    all_files = os.listdir(cur_dir)
    if rec == '':
        rec = 'w'
    with open('logfile.txt', rec, encoding='utf-8') as logfile:
        for th_file in all_files:
            if checkfilemp3(th_file):
                cur_name = th_file
                while len(th_file) >= 5:
                    if th_file[0] in symb:
                        th_file = th_file[1:]
                    else:
                        break
                record_of_change(cur_name,th_file, logfile)
    print('done')

def change_name_place(cur_dir,rec):
# меняет местами исполнителя и название
    if cur_dir == '':
        cur_dir = curr_dir()
    if rec == '':
        rec = 'w'
    all_files = os.listdir(cur_dir)
    with open('logfile.txt', rec, encoding='utf-8') as logfile:
        for th_file in all_files:
            if checkfilemp3(th_file):
                cur_name = th_file
                if th_file.count(' - ') > 0:
                    th_file = th_file[0: -4]
                    chnamelist = th_file.split(' - ')
                    th_file = chnamelist[1] + ' - ' + chnamelist[0] + '.mp3'

                record_of_change(cur_name,th_file, logfile)
        print('done')


def capitalize_name(cur_dir, rec):
# первые буквы большие - остальные маленькие
    if cur_dir == '':
        cur_dir = curr_dir()
    all_files = os.listdir(cur_dir)
    if rec == '':
        rec = 'w'
    with open('logfile.txt', rec, encoding='utf-8') as logfile:
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
                    record_of_change(cur_name,th_file, logfile)
    print('done')


def add_artists(cur_dir, rec):
# добавляет артиста спереди
    cur_dir = curr_dir()
    artist_name = cur_dir[cur_dir.rfind('\\') + 1:]
    ask_name = input('%s, подходит?' %artist_name)
    if ask_name != '':
        artist_name = ask_name
    all_files = os.listdir(cur_dir)
    with open('logfile.txt', 'w', encoding='utf-8') as logfile:
        for th_file in all_files:
            if checkfilemp3(th_file):
                cur_name = th_file
                if th_file.count(artist_name) == 0:
                    th_file = artist_name + ' - ' + th_file
                    record_of_change(cur_name,th_file, logfile)
    print('done')

def latin_to_rus(cur_dir, rec):
# меняет латинские буквы на русские
    alphabet = {"а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о",
            "п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"}
    lett4 = {'tsch':'щ',}
    lett3 = {'tch':'ч','sch':'щ',}
    lett2 = {'yo':'ё','yu':'ю','ya':'я','kh':'х','sh':'ш','zh':'ж',}
    lett1 = {'a':'а','b':'б','c':'ц','d':'д','e':'е','f':'ф','g':'г','h':'х','i':'и',
             'j':'й','k':'к','l':'л','m':'м','n':'н','o':'о','p':'п','r':'р','s':'с',
             't':'т','u':'у','v':'в','x':'кс','y':'й','z':'з','\'':'ь',}
    if cur_dir == '':
        cur_dir = curr_dir()
    if rec == '':
        rec = 'w'
    all_files = os.listdir(cur_dir)
    with open('logfile.txt', rec, encoding='utf-8') as logfile:
        for th_file in all_files:
            if checkfilemp3(th_file):
                cur_name = th_file[:]
                th_file = th_file[:-4]
                allset = (lett4, lett3, lett2, lett1)
                for myset in allset:
                    for xlett in myset:
                        th_file = th_file.lower()
                        for i in range(th_file.count(xlett)):
                            th_file = th_file.replace(xlett, myset[xlett])
                th_file = th_file + '.mp3'
                record_of_change(cur_name,th_file, logfile)
    print('done')
    capitalize_name(cur_dir, 'a')

def unchanging(cur_dir):
        # отменяет изменения
        if cur_dir == '':
            cur_dir = curr_dir()

        with open('logfile.txt', 'r', encoding='utf-8') as logfile:
            allfilesnames = logfile.readlines()
        with open('unlogfile.txt', 'w', encoding='utf-8') as unlogfile
            for i in range(len(allfilesnames) - 1, 0, -1):
                pareofnames = allfilesnames[i].split(' ;;; ')
                cur_name = pareofnames[1].strip()
                th_file = pareofnames[0].strip()
                record_of_change(cur_name, th_file, unlogfile)
        print('done')