# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

class Factory:

	def __init__(self, name, color, type):
		self.name = name
		self.color = color
		self.type = type

	def buy_stuff(self):
		print('Закупаем материал для изготовления игрушек.')

	def making_toy(self):
		print('Идет производство игрушек.')

	def painting(self):
		print('Запущен процесс окраски изделий')

toy = Factory('Медведь', 'бурый', 'animal')


# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

class Toy:

	def __init__(self, name, color):
		self.name = name
		self.color = color


class AnimalToy(Toy):

	def __init__(self, name, color):
		super().__init__(name, color)
		self.type = 'Животное'


class Cartoon(Toy):

	def __init__(self, name, color):
		super().__init__(name, color)
		self.type = 'Мультфильм'


class FactoryToys:

	def toy_create(self, name, color, toy_type):
		self._buy_stuff()
		self._making_toy()
		self._painting()
		if toy_type == 'Животное':
			return AnimalToy(name, color)
		elif toy_type == 'Мультфильм':
			return Cartoon(name, color)

	def _buy_stuff(self):
		print('Закупаем материал для изготовления игрушек.')

	def _making_toy(self):
		print('Идет производство игрушек.')

	def _painting(self):
		print('Запущен процесс окраски изделий')


fabrika = FactoryToys()
fabrika.toy_create('Медведь', 'Бурый', 'Животное')