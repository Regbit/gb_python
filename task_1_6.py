a = float(input("Enter first day results: "))
b = float(input("Enter target result: "))
factor = 0.1

progress = a
day = 1
while True:
	print(f"Day {day}: {progress:.2f}")
	if progress >= b:
		day_str = "days"
		if day == 1:
			day_str = "day"

		print(f"It will take you {day} {day_str} to achieve your goal")
		break
	progress = progress * (1 + factor)
	day = day + 1