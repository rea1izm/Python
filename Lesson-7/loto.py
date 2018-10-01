import random


class TempList():

	def __init__(self):
		self._list = []

	def _temp_list(self):
		tm_list = []
		while len(tm_list) < 15:
			x = random.randint(1, 90)
			if x not in tm_list:
				tm_list.append(x)
		self._list = tm_list
		return self._list

	def _clearing_temp_list(self):
		for i in range(5):
			self._list.pop(0)
		return self._list


class Ticket:

	def __init__(self):
		self.line = TempList._temp_list(self)
		self.short_line = []
		self.head = '===  БИЛЕТ КОМПЬЮТЕРА  =='
		self.ticket = self.generate_ticket()
		self.point = 0

	def generate_line(self):
		self.short_line = self.line[0:5]
		self.short_line.sort()
		self.line = TempList._clearing_temp_list(self)
		return self.short_line

	def create_one_line_ticket(self):
		num = self.generate_line()
		line = ['◻', '◻', '◻', '◻', '◻', '◻', '◻', '◻', '◻']
		index = []
		while len(index) < 5:
			i = random.randint(0, 8)
			if i not in index:
				index.append(i)
		index.sort()
		for a in index:
			line[a] = num[0]
			num.pop(0)
		self.short_line.clear()
		return line

	def generate_ticket(self):
		self.ticket = []
		for i in range (3):
			i = self.create_one_line_ticket()
			self.ticket.append(i)
		return self.ticket

	def print_ticket(self):
		print(self.head)
		for b in self.ticket:
			c = (f'{b[0]} {b[1]} {b[2]} {b[3]} {b[4]} {b[5]} {b[6]} {b[7]} {b[8]}')
			print(f'{c:^23}')
		print('=========================')

	def delete_num(self, qwe):
		delete = '▧'
		zte = []
		for ind_1, list_of_numbers in enumerate(self.ticket):
			if qwe in list_of_numbers:
				ind_2 = list_of_numbers.index(qwe)
				zte.append(ind_1)
				zte.append(ind_2)
				self.ticket[zte[0]][zte[1]] = delete
				self.point += 1
		return self.ticket


class YourTicket(Ticket):

	def __init__(self):
		self.line = TempList._temp_list(self)
		self.short_line = []
		self.head = '======= ВАШ БИЛЕТ ======='
		self.ticket = self.generate_ticket()
		self.point = 0
		self.answ = 0



class Loto:

	def __init__(self):
		self.bag = []
		self.len_bag = self.get_len_bag()
		self.ball = 0

	def generate_bag(self):
		bag = []
		for i in range (91):
			bag.append(i)
		bag.pop(0)
		self.bag = bag
		return self.bag

	def get_len_bag(self):
		self.len_bag = len(self.bag)
		return self.len_bag

	def get_ball(self):
		x = self.get_len_bag() - 1
		index = random.randint(1, x)
		self.ball = self.bag[index]

	def update_bag(self, ball):
		self.bag.remove(ball)
		self.len_bag = self.get_len_bag()



class Game:

	def __init__(self):
		self.player = YourTicket()
		self.enemy = Ticket()
		self.loto = Loto()

	def answer(self, ball):
		self.player.delete_num(ball)
		while True:
			try:
				choice = input('Выбирите дейсвтие:\n'
							   '1. Зачеркнуть номер\n'
							   '2. Продолжить\n'
							   '--------------------\n'
							   'Введите номер действия:')
			except ValueError:
				print('Попробуйте еще раз.')

			if choice == '1':
				self.player.answ += 1
				break
			elif choice == '2':
				break
			else:
				print('Попробуйте еще раз.')
				print('-------------------')
		return self.player.answ

	def check_point(self):
		if self.player.point == self.player.answ:
			return 1
		else:
			return 0


	def start_game(self):
		print('Добро пожаловать в PYTHON LOTO!')
		print('Удачной игры!')
		self.loto.generate_bag()
		self.player.print_ticket()
		self.enemy.print_ticket()
		while self.player.point < 15 and self.enemy.point < 15:
			self.loto.get_ball()
			ball = self.loto.ball
			self.loto.update_bag(ball)
			len_bag = self.loto.get_len_bag()
			print(f'Новый бочонок: {ball} (осталось {len_bag})')
			self.enemy.delete_num(ball)
			self.player.print_ticket()
			self.enemy.print_ticket()
			self.answer(ball)

			if self.player.point != self.player.answ:
				self.enemy.point = 15
				break

		if self.player.point == 15:
			print('Поздравляем с победой!')
		elif self.enemy.point == 15:
			print('Победу одержал компьютер!')

start = Game()
start.start_game()




