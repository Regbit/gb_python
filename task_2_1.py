some_list = ['a', 23, 723454.04, False, [4, 9], {2, 5}, {"a": 234, "b": 451}, 6 + 9j]
i = 0

for item in some_list:
	print(f'Type of item #{i}: {type(some_list[i])}')
	i += 1
