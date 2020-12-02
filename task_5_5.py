from os import path
from random import randint, random

with open(path.join("data", "task_5_5_input.txt"), mode='w+', encoding='utf-8') as file:
	# write
	lst = [round(random() * (10 ** randint(1, 3)), 2) for _ in range(randint(20, 50))]
	file.write(' '.join(str(num) for num in lst))

	# read
	file.seek(0)
	data = file.read().split()
	num_list = [float(i) for i in data]
	print(f"Sum of numbers in file = {sum(num_list)}")
