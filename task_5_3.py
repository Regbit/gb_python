from os import path

file_name = path.join("data", "task_5_3_data.txt")

try:
	with open(file_name, mode='r', encoding='utf-8') as file:
		employee_dict = dict()
		for line in file.readlines():
			try:
				employee_dict[line.split()[0]] = float(line.split()[1])
			except ValueError:
				print("Could not parse salary value!")

		small_salary_list = []
		for emp, sal in employee_dict.items():
			if sal < 20000:
				small_salary_list.append(emp)

		avg_salary = sum(employee_dict.values()) / len(employee_dict)

		print(f"Employees with a salary smaller than 20k: {', '.join(small_salary_list)}")
		print(f"Average salary is {round(avg_salary, 2)}")


except FileNotFoundError:
	print(f"File {file_name} was not found!")
