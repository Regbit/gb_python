from os import path

file_name = path.join("data", "task_5_2_data.txt")

try:
	with open(file_name, mode='r', encoding='utf-8') as file:
		word_count_list = []
		for line in file.readlines():
			word_count_list.append(len(line.split()))

		print(f"File has {len(word_count_list)} lines.")
		line_no = 1
		for cnt in word_count_list:
			print(f"Line #{line_no} has {cnt} words.")
			line_no += 1
except FileNotFoundError:
	print(f"File {file_name} was not found!")
