# file = open('001.txt')  # Считывается содержимое из файла
# text = file.read()
# file.close()  # необходимо всегда закрывать файл после окончания работы с ним
# print(file)
#
# file = open('001.txt')
# lines = file.readlines()  # каждая новая строка документа будет элементом в списке []
# file.close()
# print(lines)
#
# file = open('001.txt')
# lines = file.readlines()
# for line in lines:
# 	print(line.strip())   # убирает спецсимволы из текста (/n и т.д.)
# file.close()  # необходимо всегда закрывать файл после окончания работы с ним
#
# file = open('001.txt')
# print(file.readline())  # выводит строки по очереди 'Hello'
# print(file.readline())  # 'World'
# print(file.readline())  # '!'
# print(file.readline())  # ''
# file.close()
#
# file = open('001.txt', 'w')  # 'w' дает права на запись !!!! ПЕРЕПИСЫВАЕТ файл
# file.write('qwe')
# file.close()
#
# file = open('001.txt')
# lines = file.readlines()
# file.close()
# print(lines)

# file = open('001.txt', 'w')
# lines = ['qwe\n', 'asd\n', 'poiu']
# file.writelines(lines)
# file.close()
#
# file = open('001.txt')
# lines = file.readlines()
# file.close()
# print(lines)
#
# file = open('001.txt', 'w')
# lines = ['Hello\n', 'World\n', '!']
# file.writelines(lines)
# file.close()
#
# file = open('001.txt')
# lines = file.readlines()
# file.close()
# print(lines)

# with open('001.txt') as file:  # менеджеры контекста (позволяет открывать и работать с файлом не вводя строчку о его закрытии
# 	with open('001.txt') as file2:  # можно открыть менеджер в менеджере и на чтение и на запись
# 		print(file.read())
# 	print(file.closed)  # мы видим, что в теле менеджера файл все еще открыт False
# print(file.closed)  # мы видим, что в этот момент файл уже закрыт True

# try:						# проверка на ошибку ввода-вывода
# 	f_obj = open('001.txt')
# 	for line in f_obj:
# 		print(line)
# except IOError:
# 	print('Произошла ошибка ввода-вывода')
# finally:			# еще один элемент try-except, который будет выполнен независимот от результат
# 	f_obj.close()

# with open('001.txt', 'r+', encoding='utf-8') as f:  # в кодировке utf-8
# 	print(f.tell())  # позволяет увидеть где находится курсор
# 	print(f.read())
# 	print(f.tell())
# 	f.write('\n\nzxc\nnzxc\nzxc')
# 	print(f.tell())
# 	print(f.read())
# 	f.seek(0)  # перемещает курсор в начало файла

# with open('001.txt', 'r+') as f:
# 	print('необычная работа функции', file=f)


import os
# print(os.getcwd())  # показывает текущую рабочую директорию
# print(os.listdir())  # показывает список всех файлов в директории
# print(os.path.isdir('webinar.py'))  # 'имя файла' папка?
# print(os.path.isfile('webinar.py'))  # 'имя файла' файл?
# print(os.path.basename(r'D:\Данила\Учеба\Программирование\Geekbrains\repo\working-with-files'))  # в Windows в полных путях необх ставить в начале r или дублировать слэш(\\)
# print(os.path.splitext('webinar.py'))  # создается коретж (имя файла, расширение)
# main_folder = r'D:\Данила\Учеба\Программирование\Geekbrains\repo\working-with-files'
# folder = 'desktop'
# file_name = 'webinar1.py'
# print(os.path.join(main_folder, folder, file_name))

# import json
#
# data = {'income': {'salary': 5000, 'bonus': 2000}}  # создание и импорт в json
# with open('Vova.json', 'w', encoding='utf-8') as f_json:  # для работы кириллицы
#     json.dump(data, f_json, ensure_ascii=False)

# with open('Vova.json') as f_json:  # импорт из json
# 	data_1 = json.load(f_json)
# 	print(data_1)
# 	print(type(data_1))

# print(json.dumps(data))  # показываепт в каком виде будет импортирована инфа
# data = '{"income": {"salary": 5000, "bonus": 2000}}'
# print(json.loads(data))  # распарсивает строку и выдает словарь (в нашем случае)
# print(json.loads(data))

# import shutil
#
# shutil.copy('', '')  # скопировать файл
# shutil.copyfile('', '')  # скопировать файл с мета-данными

import sys

# sys.argv
# sys.path
# sys.exit(3)  # меняет код выхода
# print('qwe')  # не исполняется, т.к. ранее скрипт был завершен


i = 23
print(i % 10)