from random import randint


def no_duplicates(num_list):
	res = [num_list[i] for i in range(len(num_list)) if num_list.count(num_list[i]) == 1]

	print(f"Base list: {num_list}")
	print(f"Result list: {res}\n")


no_duplicates([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11])
no_duplicates([randint(1, 50) for i in range(10)])
