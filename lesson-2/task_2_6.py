item_list = []
item_structure_dict = dict()
default_item_structure_dict = {"Name": "str", "Price": "float", "Quantity": "float", "Units": "str"}
next_id = 1

print("Define item structure.")
print("1. Use default")
print("2. Enter custom structure")

command = int(input(""))

if command == 1:
	print("-" * 30)
	print("Setting standard structure.")
	item_structure_dict = default_item_structure_dict
	print(item_structure_dict)

elif command == 2:
	print("-" * 30)
	print("Enter item parameter structure.")
	print('Command format: "param_1_name":"param_1_type", "param_2_name":"param_2_type", ...')
	print('Example: Name:str, Price:float\n')
	command = input("")
	for param in command.split(","):
		item_structure_dict[param.split(":")[0].strip()] = param.split(":")[1].strip()

if len(item_structure_dict) != 0:
	while True:

		print("-" * 30)
		print("Choose an option from the menu:\n")
		print("1. Show current item list")
		print("2. Add new item")
		print("3. Delete item by ID")
		print("4. Show analytics")
		print("5. Fill item list with examples (only for default structure)")
		print("\n0. Exit")

		command = int(input(""))

		if command == 1:
			print("-" * 30)
			print("Showing items in the list:")
			for i in item_list:
				print(i)

		elif command == 2:
			print("-" * 30)
			print("Enter item parameters one by one.\n")
			item_dict = dict()

			for param, type in item_structure_dict.items():
				param_value = input(f"{param}: ")
				# TODO parse more types
				if type == "int":
					item_dict[param] = int(param_value)
				elif type == "float":
					item_dict[param] = float(param_value)
				else:
					item_dict[param] = param_value

			item_list.append((next_id, item_dict))
			next_id += 1

		elif command == 3:
			print("-" * 30)
			print("Enter ID of item you wish to delete.\n")
			id = int(input("ID: "))

			for i in item_list:
				if i[0] == id:
					item_list.remove(i)

		elif command == 4:
			print("-" * 30)
			print("Showing analytics.\n")
			analytics_dict = dict()
			for param in item_structure_dict.keys():
				analytics_dict[param] = set()
				for item in item_list:
					analytics_dict[param].add(item[1][param])

				print(f"{param}: {analytics_dict[param]}")

		elif command == 5:
			if item_structure_dict == default_item_structure_dict:
				print("-" * 30)
				print("Filling item list with examples...")
				item_list.append((1000, {"Name": "Item_1", "Price": 100000, "Quantity": 10, "Units": "u"}))
				item_list.append((2000, {"Name": "Item_2", "Price": 200000, "Quantity": 20, "Units": "u"}))
				item_list.append((3000, {"Name": "Item_3", "Price": 300000, "Quantity": 30, "Units": "u"}))
				item_list.append((4000, {"Name": "Item_4", "Price": 400000, "Quantity": 40, "Units": "u"}))

		elif command == 0:
			print("-" * 30)
			print("Exiting the program.")
			break
