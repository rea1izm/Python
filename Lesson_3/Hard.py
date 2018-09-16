# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

def attack(attaker, deffender):
	attaker_name = attaker.get('name')
	deffender_name = deffender.get('name')
	armor = int(deffender.get('armor'))
	damage = int(attaker.get('damage'))/armor
	hp = int(deffender.get('health')) - damage

	deffender.update({'health':hp})

	if hp <= 0:
		return False
	else:
		return True


def save_character(character):
	name = character.get('name')
	with open('{}.txt'.format(name), 'w') as file:
		for line in character:
			file.write('{0}={1}\n'.format(line,character.get(line)))


def load_character(name_character):
	data = ''
	value = ''
	info = {}
	with open('{0}.txt'.format(name_character), 'r') as file:
		for line in file:
			data, value = line.split('=')
			info.update({data: value.strip()})
		return info


player_name = input('Дайте имя своему персонажу: ')
player = {'name':player_name,
		  'health':110,
		  'armor' :2,
		  'damage':60}

enemy_name = input('Как зовут вашего врага: ')
enemy = {'name':enemy_name,
		 'health':120,
		 'armor':4,
		 'damage':30}

# print(attack(player, enemy))
save_character(player)
save_character(enemy)

player = load_character(player_name)
enemy = load_character(enemy_name)

fight = True
n_round = 1
while True:

	fight = attack(player, enemy)
	n_round += 1
	if fight == False:
		break
	fight = attack(enemy, player)
	n_round += 1
	if fight == False:
		break

if n_round % 2 == 0:
	print('Победу в этом бою одержал {0}!\nУ него осталось {1} здоровья.'.format(player.get('name'), player.get('health')))
else:
	print('Победу в этом бою одержал {0}!\nУ него осталось {1} здоровья.'.format(enemy.get('name'), enemy.get('health')))