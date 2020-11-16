from os import path

with open(path.join("data", "task_5_1_input.txt"), mode='w', encoding='utf-8') as file:
	while True:
		next_line = input(">")
		if next_line == '':
			break
		file.write(f"{next_line}\n")
