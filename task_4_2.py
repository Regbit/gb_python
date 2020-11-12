from random import randint


def find_all_greater_than_previous(num_list):
	res = [num_list[i] for i in range(1, len(num_list)) if num_list[i] > num_list[i-1]]

	print(f"Base list: {num_list}")
	print(f"Result list: {res}\n")


find_all_greater_than_previous([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55])
find_all_greater_than_previous([randint(1, 1000) for i in range(20)])

