some_list = []

print("Fill the list by entering some values.")
print("When you're done, hit Enter on empty line.")

while True:
	new_item = input("Enter new item: ")
	if new_item == "":
		break
	some_list.append(new_item)

print("Here's your list:", some_list)
print("Swapping each pair...")
swaps = len(some_list) // 2

for i in range(swaps):
	buffer = some_list[i * 2]
	some_list[i * 2] = some_list[i * 2 + 1]
	some_list[i * 2 + 1] = buffer

print("Here's your new list:", some_list)
