import adress_form as af
from future.moves import tkinter as tk


def add_info():
    with open('info.txt', 'a') as file:
        file.writelines(f'Фамилия: {af.entry_surname.get()}\n')
        file.writelines(f'Имя: {af.entry_name.get()}\n')
        file.writelines(f'Телефон: {af.entry_phone.get()}\n')
        file.writelines(f'Описание: {af.entry_description.get()}\n')
        file.write("\n")
        file.close()






