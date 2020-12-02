from os import path

file_name = path.join("data", "task_5_6_data.txt")
subjects_dict = dict()

try:
	with open(file_name, mode='r', encoding='utf-8') as file:
		for line in file:
			values = [int(hours.split('(')[0]) for hours in line.split(':')[1].strip().split() if hours != '-']
			subjects_dict[line.split(':')[0]] = sum(values)

except FileNotFoundError:
	print(f"File {file_name} was not found!")

print(subjects_dict)

# for subj, hrs in subjects_dict.items():
# 	print(f"{subj}: {hrs}")
