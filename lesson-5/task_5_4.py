from os import path

en_ru_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}


def translate(en_line=''):
	for en, ru in en_ru_dict.items():
		en_line = en_line.replace(en, ru)
	return en_line


source_file_name = path.join("data", "task_5_4_data.txt")
target_file_name = path.join("data", "task_5_4_res.txt")

try:
	with open(source_file_name, mode='r', encoding='utf-8') as src_file:
		with open(target_file_name, mode='w', encoding='utf-8') as tgt_file:
			for line in src_file:
				tgt_file.write(translate(line))

except FileNotFoundError:
	print(f"File {source_file_name} was not found!")
