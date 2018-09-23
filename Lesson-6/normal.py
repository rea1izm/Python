# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Person:

	def __init__(self, name, hp, dmg, ar):
		self.name = name
		self.health = hp
		self.damage = dmg
		self.armor = ar

	def _attack_mode(self, en_arm):
		if self.damage > en_arm:
			damage = self.damage - en_arm
		else:
			damage = 0
		return damage

	def defend_mode(self, damage):
		self.health = self.health - damage


class Player(Person):

	def __init__(self, name, hp, dmg, arm, spd):
		super().__init__(name, hp, dmg, arm)
		self.speed = spd


class Enemy(Person):
	def __init__(self, name, hp, dmg, arm, spd):
		super().__init__(name, hp, dmg, arm)
		self.speed = spd


class Fight:

	def __init__(self, ftr_1, ftr_2):
		self.fighter_1 = ftr_1
		self.fighter_2 = ftr_2

	def who_first(self):
		if self.fighter_1.speed >= self.fighter_2.speed:
			first = self.fighter_1
			second = self.fighter_2
		else:
			first = self.fighter_2
			second = self.fighter_1
		return first, second

	def fight_logo(self, first, second):
		damage = first._attack_mode(second.armor)
		second.defend_mode(damage)
		print(f'{first.name} нанес {damage} урона {second.name}.')
		print(f'У {second.name} осталалось {second.health} здоровья.')

	def start_game(self):
		first, second = self.who_first()
		n_round = 1
		while first.health > 0 and second.health > 0:
			print(f'Раунд {n_round} начался!')
			self.fight_logo(first, second)
			if second.health > 0:
				self.fight_logo(second, first)
			n_round += 1
			print('=============================')

		if first.health > 0:
			print(f'Победу в {n_round-1} раунде одержал {first.name}!\nУ него осталось {first.health} здоровья.')
		else:
			print(f'Победу в {n_round-1} раунде одержал {second.name}!\nУ него осталось {second.health} здоровья.')


player = Player('Довакин', 120, 28, 15, 20)
enemy = Enemy('Гоблин', 145, 23, 17, 15)
fight = Fight(player, enemy)
fight.start_game()


