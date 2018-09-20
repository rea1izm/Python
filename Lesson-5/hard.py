# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.


# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil
print('sys.argv = ', sys.argv)


def print_help():
	print("help - получение справки")
	print("mkdir <dir_name> - создание директории")
	print("ping - тестовый ключ")
	print('cp <file_name> - создает копию указанного файла')
	print("rm <file_name> - удаляет указанный файл")
	print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
	print("ls - отображение полного пути текущей директории")



def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


def copy_file():
	filename = sys.argv[2]
	name, res = filename.split('.')
	new_file_name = f'{name}_copy.{res}'
	shutil.copy(filename, new_file_name)
	print(f'Файл {new_file_name} успешно создан.')


def remove_file():
	filename = sys.argv[2]
	if os.path.exists(filename):
		answer = input(f'Вы действительно ходите удалить {filename} файл? Y/N? ')
		if answer == 'Y':
			os.remove(filename)
			print(f'Файл {filename} успешно удален.')
		elif answer == 'N':
			print(f'Процесс удаления файла {filename} прерван.')
		else:
			print('Введена неверная команда.')
	else:
		print(f'Невозможно удалить {filename}, файл не найден.')



def change_dir():
	name = sys.argv[2]
	try:
		os.chdir(name)
		print(f'\nВы успешно перешли в папку: {name}\n')
	except FileNotFoundError:
		print(f'Папка {name} не найдена.\n')


def full_path_dir():
	dir = os.getcwd()
	print(dir)


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
	"cp": copy_file,
	"rm": remove_file,
	"cd": change_dir,
	"ls": full_path_dir
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")