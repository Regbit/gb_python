line = input("Enter some text: ")

words = line.split()

for i in enumerate(words):
	print(f"#{i[0]}: {i[1][:10]}")
