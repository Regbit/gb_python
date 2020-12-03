from os import path
import json

source_file_name = path.join("data", "task_5_7_data.txt")
target_file_name = path.join("data", "task_5_7_res.json")
companies_dict = dict()

try:
	with open(source_file_name, mode='r', encoding='utf-8') as file:
		for line in file:
			companies_dict[line.split()[0]] = (tuple(line.split()[1:4]))

except FileNotFoundError:
	print(f"File {source_file_name} was not found!")

profit_dict = dict()
positive_profit_cnt, positive_profit_sum = 0, 0

for comp, data in companies_dict.items():
	profit = float(data[1]) - float(data[2])
	profit_dict[comp] = profit
	if profit > 0:
		positive_profit_cnt += 1
		positive_profit_sum += profit

avg_profit = {"average_profit": positive_profit_sum / positive_profit_cnt}

output_list = [profit_dict, avg_profit]

with open(target_file_name, mode='w', encoding='utf-8') as file:
	json.dump(output_list, file, indent=4, ensure_ascii=False)
