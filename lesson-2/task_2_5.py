ratings_list = []

print("Enter integer ratings values one by one.")
print("When you're done, hit Enter on empty line.")

while True:
	new_item = input("Enter new item: ")
	if new_item == "":
		break

	insert_at = None
	new_item = int(new_item)

	for i in range(len(ratings_list)):
		if new_item >= ratings_list[i]:
			insert_at = i
			break

	if insert_at is None:
		ratings_list.append(new_item)
	else:
		ratings_list.insert(insert_at, new_item)

	print("Ratings list:", ratings_list)
