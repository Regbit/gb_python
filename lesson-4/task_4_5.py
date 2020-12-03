from functools import reduce

num_list = (i for i in range(100, 1000+1) if i % 2 == 0)


def multiply(a, b):
	return a * b


print(reduce(multiply, num_list))
