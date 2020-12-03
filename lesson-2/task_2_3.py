month = int(input("Enter a valid month number: "))

seasons_dict = {"Winter": [12, 1, 2], "Spring": [3, 4, 5], "Summer": [6, 7, 8], "Autumn": [9, 10, 11]}

for k, v in seasons_dict.items():
	if month in v:
		print(k)
