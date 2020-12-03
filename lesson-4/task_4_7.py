from functools import reduce


def multiply(a, b):
	return a * b


def fact(n):
	for i in range(1, n + 1):
		yield range(1, i + 1) if i != 0 else [1]


def parse_int(input_text="Enter a valid integer: "):
	input_num = None
	while input_num is None:
		try:
			input_num = int(input(input_text))
		except ValueError:
			print(f"Invalid input value!")

	return input_num


for el in fact(parse_int()):
	print(f"{len(el)}! = {' * '.join(str(i) for i in el)} = {reduce(multiply, el)}")
