# 1) Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

new_file = open("new_file.txt", "w", encoding='utf-8')
lists = ['первая строка\n', 'вторая строка\n', 'третья строка\n']
new_file.writelines(lists)
new_file.close()
