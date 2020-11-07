def parse_numbers_string_to_list(numbers_str=''):
	"""Take a string and returns all numbers from it."""
	new_numbers = []
	for num in numbers_str.replace('!', '').split():
		try:
			new_numbers.append(float(num))
		except ValueError:
			pass

	return new_numbers


exit_flag = False
numbers = []

while not exit_flag:
	numbers_str = input("Enter a line of numbers separated by spaces."
					 "\nIf you want to exit, type '!' in the end of the line\n").strip()

	exit_flag = numbers_str[-1] == '!'
	numbers += parse_numbers_string_to_list(numbers_str)
	print(f"Sum of {numbers} is {sum(numbers)}")
