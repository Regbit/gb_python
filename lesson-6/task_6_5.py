class Stationery:

	def __init__(self, title):
		self.title = title

	def draw(self):
		print("Запуск отрисовки.")


class Pen(Stationery):

	def __init__(self):
		super().__init__("Pen")

	def draw(self):
		print("Запуск отрисовки ручкой.")


class Pencil(Stationery):

	def __init__(self):
		super().__init__("Pencil")

	def draw(self):
		print("Запуск отрисовки карандашом.")


class Handle(Stationery):

	def __init__(self):
		super().__init__("Handle")

	def draw(self):
		print("Запуск отрисовки маркером.")


pen = Pen()
pencil = Pencil()
handle = Handle()

pen.draw()
pencil.draw()
handle.draw()
