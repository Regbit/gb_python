def my_func(x, y):
	"""my_func(x, y) -> float"""
	if (type(x) is not int and type(x) is not float) or x <= 0:
		return f"'x' must be positive integer or float! x = {x, type(x)}"

	if type(y) is not int or y >= 0:
		return f"'y' must be negative integer! y = {y, type(y)}"

	res = x
	for i in range(-y-1):
		res *= x

	return 1/res


print(my_func(2.0, -4))
