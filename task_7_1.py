from itertools import product


class Matrix:

	def __init__(self, matrix_data=None):
		self.matrix_data = matrix_data

	@property
	def rows_count(self):
		return len(self.matrix_data if self.matrix_data else 0)

	@property
	def columns_count(self):
		return len(self.matrix_data[0] if self.matrix_data and self.matrix_data[0] else 0)

	def __str__(self):
		out = ''

		if self.matrix_data:
			out = '\n'.join('|' + ' '.join([str(num) for num in row]) + '|' for row in self.matrix_data)

		return out

	def add_sub(self, other, mul=1):
		if self.rows_count == other.rows_count and self.columns_count == other.columns_count:
			out = [[0 for _ in range(self.columns_count)] for _ in range(self.rows_count)]
			for i, j in product(list(range(self.rows_count)), list(range(self.columns_count))):
				out[i][j] = self.matrix_data[i][j] + mul * other.matrix_data[i][j]

			return Matrix(out)
		else:
			return f"Matrices must have the same dimensions!" \
				   f"\nMatrix 1 is {self.rows_count}x{self.columns_count}" \
				   f"\nMatrix 2 is {other.rows_count}x{other.columns_count}"

	def __add__(self, other):
		return self.add_sub(other)

	def __sub__(self, other):
		return self.add_sub(other, -1)


def new_matrix(matrix_data):
	print(f"Attempting to make matrix from data:{matrix_data}")
	if matrix_data and type(matrix_data) == list and len(matrix_data[0]):
		for row in matrix_data:
			if len(row) != len(matrix_data[0]):
				return "All rows must contain the same number of elements!" + \
					   f"\nFirst row elements count: {len(matrix_data[0])}" + \
					   f"\nThis row elements count: {len(row)}"
		return Matrix(matrix_data)

	return f"Could not make matrix from input data!\nData: {matrix_data}"


mx = new_matrix([[1, 2], [3, 4, 5]])
print(mx, end='\n\n')

mx = new_matrix([])
print(mx, end='\n\n')

mx_1 = new_matrix([[2, 1], [3, 5]])
print(f"mx_1:\n{mx_1}", end='\n\n')

mx_2 = new_matrix([[4, 6], [2, -3]])
print(f"mx_2:\n{mx_2}", end='\n\n')

mx_3 = new_matrix([[1, 5, 13], [-9, 4, 3]])
print(f"mx_3:\n{mx_3}", end='\n\n')

mx_4 = new_matrix([[9, 6, -10], [4, 1, 1]])
print(f"mx_4:\n{mx_4}", end='\n\n')

print(f"mx_1 + mx_2:\n{mx_1 + mx_2}", end='\n\n')
print(f"mx_1 + mx_3:\n{mx_1 + mx_3}", end='\n\n')
print(f"mx_3 + mx_4:\n{mx_3 + mx_4}", end='\n\n')
print(f"mx_1 - mx_2:\n{mx_1 - mx_2}", end='\n\n')
