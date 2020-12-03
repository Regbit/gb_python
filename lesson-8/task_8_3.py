class NonNumberElementError(Exception):
	pass


def check(num_line: str):
	if num_line.isdigit():
		return int(num_line)
	else:
		raise NonNumberElementError("an element must be integer")


line = input('>')
num_list = []

while line:
	try:
		num_list.append(check(line))
	except NonNumberElementError as err:
		print(f"Error: {err}")

	print(f"Numbers list: {num_list}")
	line = input('>')
