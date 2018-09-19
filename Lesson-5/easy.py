# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import shutil
import sys

def create_directory(dir_name):
	try:
		os.mkdir(dir_name)
		print(f'Успешно создано: {dir_name}')
	except FileExistsError:
		print(f'Невозможно создать: {dir_name}')

def delete_directory(dir_name):
	try:
		os.rmdir(dir_name)
		print(f'Успешно удалено: {dir_name}')
	except FileNotFoundError:
		print(f'Невозможно удалить: {dir_name}')


# name_folder = 'dir'
# a = 1
# b = 1
# for _ in range(9):
# 	name = (f'{name_folder}_{a}')
# 	create_directory(name)
# 	a += 1
#
# for _ in range(9):
# 	name = (f'{name_folder}_{b}')
# 	delete_directory(name)
# 	b += 1


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def list_dir():
	current_folder = os.listdir()
	print('Папки данного каталога:')
	for i in current_folder:
		if os.path.isdir(i):
			print(i)
#
# list_dir()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_work_file():
	filename = sys.argv[0]
	name, res = filename.split('.')
	new_file_name = f'{name}_copy.{res}'
	shutil.copy(filename, new_file_name)