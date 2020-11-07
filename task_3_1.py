def div(a=0.0, b=1.0):
	"""div(a=0.0, b=1.0) -> float

	Positional args:
	a -- dividend (default 0.0)
	b -- divisor (default 1.0)
	"""
	try:
		return a / b
	except ZeroDivisionError:
		return "Cant divide by 0!"


def input_num(input_text="Enter a valid number: "):
	"""input_num(input_text="Enter a valid number: ") -> float"""
	while True:
		try:
			return float(input(input_text))
		except ValueError:
			print("Enter a VALID number!")


print(div(
	input_num("Enter dividend: "),
	input_num("Enter divisor: ")
))
