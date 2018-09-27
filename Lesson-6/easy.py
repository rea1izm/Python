# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)


class TownCar:

	def __init__(self, speed, color, name):
		self.speed = speed
		self.color = color
		self.name = name
		self.is_polise = False

	def go(self):
		print(self.name, 'начал движение...')

	def stop(self):
		print(self.name, 'совершил остановку')

	def turn(self, direction):
		if direction == 'left':
			print(self.name, 'повернул налево')
		elif direction == 'right':
			print(self.name, 'повернул направо')
		else:
			print(self.name, 'совершил остановку')


class SportCar:

	def __init__(self, speed, color, name):
		self.speed = speed
		self.color = color
		self.name = name
		self.is_polise = False

	def go(self):
		print(self.name, 'начал движение...')

	def stop(self):
		print(self.name, 'совершил остановку')

	def turn(self, direction):
		if direction == 'left':
			print(self.name, 'повернул налево')
		elif direction == 'right':
			print(self.name, 'повернул направо')
		else:
			print(self.name, 'совершил остановку')


class WorkCar:

	def __init__(self, speed, color, name):
		self.speed = speed
		self.color = color
		self.name = name
		self.is_polise = False

	def go(self):
		print(self.name, 'начал движение...')

	def stop(self):
		print(self.name, 'совершил остановку')

	def turn(self, direction):
		if direction == 'left':
			print(self.name, 'повернул налево')
		elif direction == 'right':
			print(self.name, 'повернул направо')
		else:
			print(self.name, 'совершил остановку')


class PoliceCar:

	def __init__(self, speed, color, name):
		self.speed = speed
		self.color = color
		self.name = name
		self.is_polise = True

	def go(self):
		print(self.name, 'начал движение...')

	def stop(self):
		print(self.name, 'совершил остановку')

	def turn(self, direction):
		if direction == 'left':
			print(self.name, 'повернул налево')
		elif direction == 'right':
			print(self.name, 'повернул направо')
		else:
			print(self.name, 'совершил остановку')


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class TestCar:

	def __init__(self, speed, color, name):
		self.speed = speed
		self.color = color
		self.name = name

	def go(self):
		print(self.name, 'начал движение...')

	def stop(self):
		print(self.name, 'совершил остановку')

	def turn(self, direction):
		if direction == 'left':
			print(self.name, 'повернул налево')
		elif direction == 'right':
			print(self.name, 'повернул направо')
		else:
			print(self.name, 'совершил остановку')


class TownCar2(TestCar):
	def __init__(self, speed, color, name):
		super().__init__(speed, color, name)
		self.is_police = False


class SportCar2(TestCar):
	def __init__(self, speed, color, name):
		super().__init__(speed, color, name)
		self.is_police = False


class WorkCar2(TestCar):
	def __init__(self, speed, color, name):
		super().__init__(speed, color, name)
		self.is_police = False


class PoliceCar2(TestCar):

	def __init__(self, speed, color, name):
		super().__init__(speed, color, name)
		self.is_police = True

