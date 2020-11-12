from itertools import count, cycle


def parse_int(input_text="Enter a valid integer: "):
	input_num = None
	while input_num is None:
		try:
			input_num = int(input(input_text))
		except ValueError:
			print(f"Invalid input value!")

	return input_num


exit_count = False

count_start = parse_int("Enter a valid integer to set start number: ")
count_end = None

while count_end is None or count_end < count_start:
	count_end = parse_int("Enter a valid integer to set end number (must be greater or equal than start number): ")

count_iter = count(count_start)
cycle_iter = cycle(["To be", "Not to be"])

cnt = None

while not cnt == count_end:

	cnt = next(count_iter)

	print(f"\n# {cnt}")
	print(f"Cycling through options {abs(cnt)} times:")
	cycle_count = 0
	while cycle_count != abs(cnt):
		print(f"\t{cycle_count+1}) {next(cycle_iter)}")
		cycle_count += 1
