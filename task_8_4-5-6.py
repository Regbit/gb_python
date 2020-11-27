class ModelNotFoundError(Exception):
	pass


class OfficeEquipment:

	model_info_dict = {

		# Printer
		# HP
		'I10330': {
			'equipment_type': 'printer',
			'brand': 'HP',
			'volume_l': 12.75,
			'paper_size': 'A4',
			'manufacture_year': 2014,
			'printer_type': 'Ink'
		},
		'I10331': {
			'equipment_type': 'printer',
			'brand': 'HP',
			'volume_l': 13.15,
			'paper_size': 'A4',
			'manufacture_year': 2015,
			'printer_type': 'Ink'
		},
		'P50450': {
			'equipment_type': 'printer',
			'brand': 'HP',
			'volume_l': 24.35,
			'paper_size': 'A3',
			'manufacture_year': 2018,
			'printer_type': 'Laser'
		},
		'P50455': {
			'equipment_type': 'printer',
			'brand': 'HP',
			'volume_l': 21.95,
			'paper_size': 'A3',
			'manufacture_year': 2018,
			'printer_type': 'Laser'
		},

		# Xerox
		'3300LZ': {
			'equipment_type': 'printer',
			'brand': 'Xerox',
			'volume_l': 12.35,
			'paper_size': 'A4',
			'manufacture_year': 2017,
			'printer_type': 'Ink'
		},
		'5400LZ': {
			'equipment_type': 'printer',
			'brand': 'Xerox',
			'volume_l': 11.05,
			'paper_size': 'A4',
			'manufacture_year': 2018,
			'printer_type': 'Ink'
		},

		# Canon
		'76-90': {
			'equipment_type': 'printer',
			'brand': 'Canon',
			'volume_l': 34.85,
			'paper_size': 'A3',
			'manufacture_year': 2019,
			'printer_type': 'Laser'
		},
		'36-50': {
			'equipment_type': 'printer',
			'brand': 'Canon',
			'volume_l': 10.05,
			'paper_size': 'A4',
			'manufacture_year': 2019,
			'printer_type': 'Laser'
		},

		# Epson
		'5505-9': {
			'equipment_type': 'printer',
			'brand': 'Epson',
			'volume_l': 8.15,
			'paper_size': 'A4',
			'manufacture_year': 2020,
			'printer_type': 'Ink'
		},
		'9806-5': {
			'equipment_type': 'printer',
			'brand': 'Epson',
			'volume_l': 13.55,
			'paper_size': 'A4',
			'manufacture_year': 2020,
			'printer_type': 'Laser'
		},
		'0150-S': {
			'equipment_type': 'printer',
			'brand': 'Epson',
			'volume_l': 27.75,
			'paper_size': 'A3',
			'manufacture_year': 2020,
			'printer_type': 'Laser'
		},

		# KYOCERA
		'JL56/5': {
			'equipment_type': 'printer',
			'brand': 'KYOCERA',
			'volume_l': 8.6,
			'paper_size': 'A4',
			'manufacture_year': 2020,
			'printer_type': 'Laser'
		},
		'JD80/7': {
			'equipment_type': 'printer',
			'brand': 'KYOCERA',
			'volume_l': 10.2,
			'paper_size': 'A4',
			'manufacture_year': 2019,
			'printer_type': 'Laser'
		},

		# Scanner
		# HP
		'S30310': {
			'equipment_type': 'scanner',
			'brand': 'HP',
			'volume_l': 9.75,
			'paper_size': 'A4',
			'manufacture_year': 2015,
			'scanner_sensor_type': 'CIS'
		},

		# Xerox
		'1100SS': {
			'equipment_type': 'scanner',
			'brand': 'Xerox',
			'volume_l': 8.35,
			'paper_size': 'A4',
			'manufacture_year': 2018,
			'scanner_sensor_type': 'CIS'
		},

		# Canon
		'S0-40': {
			'equipment_type': 'scanner',
			'brand': 'Canon',
			'volume_l': 11.05,
			'paper_size': 'A3',
			'manufacture_year': 2019,
			'scanner_sensor_type': 'CMOS'
		},

		# Epson
		'1010-4-S': {
			'equipment_type': 'scanner',
			'brand': 'Epson',
			'volume_l': 7.95,
			'paper_size': 'A4',
			'manufacture_year': 2020,
			'scanner_sensor_type': 'CMOS'
		},

		# KYOCERA
		'SC15/0': {
			'equipment_type': 'scanner',
			'brand': 'KYOCERA',
			'volume_l': 7.75,
			'paper_size': 'A4',
			'manufacture_year': 2020,
			'scanner_sensor_type': 'CIS'
		},

		# Copier
		# HP
		'C11490': {
			'equipment_type': 'copier',
			'brand': 'HP',
			'volume_l': 35.05,
			'paper_size': 'A4',
			'manufacture_year': 2018,
			'copier_capacity': 'up to 500 sheets'
		},

		# Xerox
		'5550CP': {
			'equipment_type': 'copier',
			'brand': 'Xerox',
			'volume_l': 36.6,
			'paper_size': 'A4',
			'manufacture_year': 2019,
			'copier_capacity': 'up to 500 sheets'
		},

		# Canon
		'C5-35': {
			'equipment_type': 'copier',
			'brand': 'Canon',
			'volume_l': 37.05,
			'paper_size': 'A4',
			'manufacture_year': 2019,
			'copier_capacity': 'up to 1000 sheets'
		},

		# Epson
		'3990-7-C': {
			'equipment_type': 'copier',
			'brand': 'Epson',
			'volume_l': 49.10,
			'paper_size': 'A3',
			'manufacture_year': 2020,
			'copier_capacity': 'up to 1000 sheets'
		},

		# KYOCERA
		'СOЗ25/3': {
			'equipment_type': 'copier',
			'brand': 'KYOCERA',
			'volume_l': 45.75,
			'paper_size': 'A3',
			'manufacture_year': 2019,
			'copier_capacity': 'up to 500 sheets'
		}
	}

	@classmethod
	def model_info(cls, model: str, equipment_type: str):
		if model in cls.model_info_dict and cls.model_info_dict[model].get('equipment_type') == equipment_type:
			return cls.model_info_dict.get(model)
		else:
			raise ModelNotFoundError(f"model '{model}' was not found in {equipment_type} dictionary")

	@classmethod
	def make(cls, model: str):
		try:
			return cls(**{'model': model, **cls.model_info(model, cls.__name__.lower())})
		except ModelNotFoundError as err:
			print(f"Can not make '{cls.__name__}':\n\t{err}")

	def __init__(self, **kwargs):
		self.model = kwargs.get('model') or 'N/A'
		self.brand = kwargs.get('brand') or 'N/A'
		self.volume_l = kwargs.get('volume_l') or 0.0
		self.paper_size = kwargs.get('paper_size') or 'N/A'
		self.manufacture_year = kwargs.get('manufacture_year') or 2000

	def __str__(self):
		return f"{self.__class__.__name__}: {self.brand} {self.model} - " \
			   f"P:{self.paper_size}; Y:{self.manufacture_year}; V:{self.volume_l}"


class Printer(OfficeEquipment):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.printer_type = kwargs.get('printer_type') or 'N/A'

	def __str__(self):
		return f"{super().__str__()}; T:{self.printer_type}"


class Scanner(OfficeEquipment):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.scanner_sensor_type = kwargs.get('scanner_sensor_type') or 'N/A'

	def __str__(self):
		return f"{super().__str__()}; T:{self.scanner_sensor_type}"


class Copier(OfficeEquipment):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.copier_capacity = kwargs.get('copier_capacity') or 'N/A'

	def __str__(self):
		return f"{super().__str__()}; C:{self.copier_capacity}"


class Warehouse:

	next_id = 1

	def __init__(self, capacity_l=0.0):
		self.capacity_l = capacity_l
		self.items = []

	@property
	def occupied_space(self):
		return round(sum([eq[1].volume_l for eq in self.items]), 3)

	def store(self, eq: OfficeEquipment):
		if self.occupied_space + eq.volume_l <= self.capacity_l:
			self.items.append((self.next_id, eq))
			self.next_id += 1

	def transfer(self):
		pass


w = Warehouse(100000)
w.store(Printer.make('9806-5'))
w.store(Scanner.make('S30310'))
w.store(Copier.make('5550CP'))


while True:

	print("-" * 30)
	print("Choose an option from the menu:\n")
	print("1. Show current item list")
	print("2. Add new item")
	print("3. Delete item by ID")
	print("4. Show analytics")
	print("\n0. Exit")

	command = int(input(""))

	if command == 1:
		print("-" * 30)
		print("Showing items in the list:")
		for i, eq in w.items:
			print(i, eq)

	elif command == 2:
		print("-" * 30)
		# print("Enter item parameters one by one.\n")
		# item_dict = dict()
		#
		# for param, type in item_structure_dict.items():
		# 	param_value = input(f"{param}: ")
		# 	# TODO parse more types
		# 	if type == "int":
		# 		item_dict[param] = int(param_value)
		# 	elif type == "float":
		# 		item_dict[param] = float(param_value)
		# 	else:
		# 		item_dict[param] = param_value
		#
		# item_list.append((next_id, item_dict))
		# next_id += 1

	elif command == 3:
		print("-" * 30)
		# print("Enter ID of item you wish to delete.\n")
		# id = int(input("ID: "))
		#
		# for i in item_list:
		# 	if i[0] == id:
		# 		item_list.remove(i)

	elif command == 4:
		print("-" * 30)
		# print("Showing analytics.\n")
		# analytics_dict = dict()
		# for param in item_structure_dict.keys():
		# 	analytics_dict[param] = set()
		# 	for item in item_list:
		# 		analytics_dict[param].add(item[1][param])
		#
		# 	print(f"{param}: {analytics_dict[param]}")

	elif command == 0:
		print("-" * 30)
		print("Exiting the program.")
		break
