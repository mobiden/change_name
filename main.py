import os
from util import *
from tkinter import filedialog as fd





answ = int(input("Удалять цифры спереди - 1:, "
                 "Переставить местами - 2:, "
                 "Все буквы, кроме первой строчные - 3:. Номер? "))
if answ == 1:
    del_fig()
elif answ == 2:
    change_name_place()
elif answ == 3:
    capitalize_name()

