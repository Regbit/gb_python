class Cell:

	def __init__(self, cell_count=1):
		self.cell_count = cell_count

	def __str__(self):
		return f"Cells: {self.cell_count}"

	def __add__(self, other):
		return Cell(self.cell_count + other.cell_count)

	def __sub__(self, other):
		if self.cell_count - other.cell_count > 0:
			return Cell(self.cell_count - other.cell_count)
		else:
			print(f"Subtraction can only result in positive value!")

	def __mul__(self, other):
		return Cell(self.cell_count * other.cell_count)

	def __floordiv__(self, other):
		if self.cell_count // other.cell_count > 0:
			return Cell(self.cell_count // other.cell_count)
		else:
			print(f"Division can only result in positive value!")

	def make_order(self, cells_per_row=1):
		return '\n'.join(['*' * (cells_per_row if i < self.cell_count // cells_per_row else self.cell_count % cells_per_row) for i in range(self.cell_count // cells_per_row + 1)])


def new_cell(cell_count):
	if type(cell_count) == int and cell_count > 0:
		return Cell(cell_count)
	else:
		print(f"Incorrect input value! Value: {cell_count}")


cell = new_cell(1)
print(cell, end='\n\n')

cell = new_cell(0)
print(cell, end='\n\n')

cell = new_cell('asd')
print(cell, end='\n\n')

cell = new_cell(3.4)
print(cell, end='\n\n')

cell_1 = new_cell(13)
cell_2 = new_cell(11)

print(f"cell_1 + cell_2 = {cell_1 + cell_2}", end='\n\n')
print(f"cell_1 - cell_2 = {cell_1 - cell_2}", end='\n\n')
print(f"cell_2 - cell_1 = {cell_2 - cell_1}", end='\n\n')

print(f"cell_1 * cell_2 = {cell_1 * cell_2}", end='\n\n')
print(f"cell_1 // cell_2 = {cell_1 // cell_2}", end='\n\n')
print(f"cell_2 // cell_1 = {cell_2 // cell_1}", end='\n\n')


print(f"{cell_1} ordered by 3 in a row:\n{cell_1.make_order(3)}", end='\n\n')
print(f"{cell_2} ordered by 7 in a row:\n{cell_2.make_order(7)}", end='\n\n')

cell_3 = cell_1 * cell_2
print(f"{cell_3} ordered by 21 in a row:\n{cell_3.make_order(21)}", end='\n\n')
