from sys import argv


def parse_num(input_num):
	try:
		return float(input_num)
	except ValueError:
		print(f"Input value must be a valid float! Value: {input_num}")
		raise ValueError


def calc_salary(hours_worked=0.0, salary_rate=0.0, bonus=0.0):
	return round((hours_worked * salary_rate) + bonus, 2)


def main(args):
	if len(args) != 4:
		print("Method accepts exactly 3 float values!")
		return
	try:
		print("Total salary =", calc_salary(parse_num(args[1]), parse_num(args[2]), parse_num(args[3])))
	except ValueError:
		print("Can not calculate salary!")


main(argv)
