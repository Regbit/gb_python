class Worker:

	def __init__(self, name, surname, position='', wage=0, bonus=0):
		self.name = name
		self.surname = surname
		self.position = position
		self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

	def get_full_name(self):
		return f"{self.name} {self.surname}"

	def get_total_income(self):
		return self._income['wage'] + self._income['bonus']


positions_list = list()
positions_list.append(Position('Ivan', 'Ivanov', 'Accountant', 100000, 25000))
positions_list.append(Position('Andrei', 'Andreev', 'Manager', 115000, 32000))
positions_list.append(Position('Sergei', 'Sergeev', 'Janitor', 55000, 10000))

for pos in positions_list:
	print(f"{pos.get_full_name()}: {pos.get_total_income()}")
