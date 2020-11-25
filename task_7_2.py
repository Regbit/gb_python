from abc import ABC, abstractmethod


class Clothes(ABC):

	def __init__(self, name):
		self.name = name

	@abstractmethod
	def required_cloth(self):
		raise NotImplementedError


class Coat(Clothes):

	def __init__(self, name, size):
		super().__init__(name)
		self.size = size

	@property
	def required_cloth(self):
		return round(self.size / 6.5 + 0.5, 3)


class Suit(Clothes):

	def __init__(self, name, height):
		super().__init__(name)
		self.height = height

	@property
	def required_cloth(self):
		return round(self.height * 2 + 0.3, 3)


clothes_list = list()
clothes_list.append(Coat("Good Leather Coat", 44))
clothes_list.append(Suit("Gentlemen Suit", 1.78))

for cl in clothes_list:
	print(f'"{cl.name}" requires {cl.required_cloth}m2 of material.')
