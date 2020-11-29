from random import randint


class ModelNotFoundError(Exception):
	pass


class StorageOverflowError(Exception):
	pass


class NotEnoughEquipmentUnits(Exception):
	pass


class DepartmentNotFoundError(Exception):
	pass


class OfficeEquipment:

	"""
	OfficeEquipment
	:param base_structure_dict: {parameter: (type, accepted_values_dict)}
	"""

	structure_dict = {
		'equipment_type': ('printer', 'scanner' 'copier'),
		'brand': ('',),
		'volume_l': (0.01, 200.0),
		'paper_size': ('A4', 'A3'),
		'manufacture_year': (2000, 2020)
	}

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

	@classmethod
	def make_any(cls, model: str):
		model_class = globals()[cls.model_info_dict[model].get('equipment_type').capitalize()]
		try:
			return model_class(**{'model': model, **cls.model_info(model, model_class.__name__.lower())})
		except ModelNotFoundError as err:
			print(f"Can not make '{model_class.__name__}':\n\t{err}")

	@classmethod
	def model_info_list(cls):
		return [(model, info) for model, info in cls.model_info_dict.items()]

	def __init__(self, **kwargs):
		self.model = kwargs.get('model') or 'N/A'
		self.brand = kwargs.get('brand') or 'N/A'
		self.volume_l = kwargs.get('volume_l') or 0.0
		self.paper_size = kwargs.get('paper_size') or 'N/A'
		self.manufacture_year = kwargs.get('manufacture_year') or 2000

	def __str__(self):
		return f"{self.__class__.__name__}: {self.brand} {self.model}"

	@property
	def full_info(self):
		return f"{self.__class__.__name__}: {self.brand} {self.model} - " \
			   f"P:{self.paper_size}; Y:{self.manufacture_year}; V:{self.volume_l}"


class Printer(OfficeEquipment):

	structure_dict = OfficeEquipment.structure_dict.copy()
	structure_dict['printer_type'] = ('Ink', 'Laser')

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.printer_type = kwargs.get('printer_type') or 'N/A'

	@property
	def full_info(self):
		return f"{super().full_info}; T:{self.printer_type}"


class Scanner(OfficeEquipment):

	structure_dict = OfficeEquipment.structure_dict.copy()
	structure_dict['scanner_sensor_type'] = ('CMOS', 'CIS', 'CCD')

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.scanner_sensor_type = kwargs.get('scanner_sensor_type') or 'N/A'

	@property
	def full_info(self):
		return f"{super().full_info}; T:{self.scanner_sensor_type}"


class Copier(OfficeEquipment):

	structure_dict = OfficeEquipment.structure_dict.copy()
	structure_dict['copier_capacity'] = ('up to 500 sheets', 'up to 1000 sheets')

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.copier_capacity = kwargs.get('copier_capacity') or 'N/A'

	@property
	def full_info(self):
		return f"{super().full_info}; C:{self.copier_capacity}"


class Department:

	equipment_list = []

	def __init__(self, name: str):
		self.name = name

	def __str__(self):
		return self.name


class Warehouse:

	next_id = 1

	def __init__(self, capacity_m3=0.0):
		self.capacity_m3 = capacity_m3
		self.equipment_list = []

	@property
	def occupied_space_m3(self):
		return round(sum([equipment[1].volume_l for equipment in self.equipment_list]) / 1000, 3)

	@property
	def count_by_model(self):
		out = {}
		for _, equipment in self.equipment_list:
			if equipment.model not in out:
				out[equipment.model] = 1
			else:
				out[equipment.model] += 1

		return out

	def store(self, equipment_model: str, quantity=1):
		if equipment_model not in OfficeEquipment.model_info_dict:
			raise ModelNotFoundError

		if self.occupied_space_m3 + OfficeEquipment.model_info_dict[equipment_model].get('volume_l') / 1000 * quantity <= self.capacity_m3:
			for i in range(quantity):
				self.equipment_list.append((self.next_id, OfficeEquipment.make_any(equipment_model)))
				self.next_id += 1
		else:
			raise StorageOverflowError

	def transfer(self, equipment_model: str, department: str, quantity=1):
		if equipment_model not in OfficeEquipment.model_info_dict:
			raise ModelNotFoundError
		if department not in department_dict:
			raise DepartmentNotFoundError

		if self.count_by_model[equipment_model] >= quantity:
			for _ in range(quantity):
				for i in range(len(self.equipment_list)):
					if self.equipment_list[i][1].model == equipment_model:
						department_dict[department].equipment_list.append(self.equipment_list.pop(i))
						break

		else:
			raise NotEnoughEquipmentUnits

	def fill_random(self):
		model_list = list(OfficeEquipment.model_info_dict.keys())
		for i in range(randint(10, 18)):
			self.store(model_list.pop(randint(0, len(model_list) - 1)), randint(15, 70))


def input_check(text='> ', input_type=int, accepted_values_range=None, accepted_values_dict=None):
	while True:
		try:
			i = input_type(input(text))
			if accepted_values_range and not (accepted_values_range[0] <= i <= accepted_values_range[1]):
				raise ValueError
			if accepted_values_dict and i not in accepted_values_dict:
				raise ValueError
			return i
		except ValueError:
			print("Enter a valid option!")


def stored_equipment_menu():
	print("-" * 30)
	print("Equipment stored in warehouse:")
	for model, qty in w.count_by_model.items():
		info = OfficeEquipment.model_info_dict[model]
		print(f"\u25b8{info.get('equipment_type').capitalize()} {info.get('brand')} {model}: {qty} unit{'s' if qty > 1 else ''}")

	percent = round(w.occupied_space_m3 / w.capacity_m3 * 100)
	print(f"\nOccupied space and capacity: {w.occupied_space_m3}/{w.capacity_m3}m3 = {percent}% filled")
	print('\u25A0' * (percent // 5) + '\u25A1' * (20 - percent // 5))


def new_model_menu():
	pass


def store_menu():
	print("-" * 30)
	print("Choose a model from the list to store:")
	i = 1
	for model, info in OfficeEquipment.model_info_list():
		print(f"{i}: {info.get('equipment_type').capitalize()} {info.get('brand')} {model}")
		i += 1

	command = input_check(accepted_values_range=[1, i-1])
	# TODO implement new_model_menu()
	# if command == i:
	# 	new_model_menu()

	model = OfficeEquipment.model_info_list()[command - 1][0]
	print("How much you wish to store?")
	while True:
		try:
			w.store(model, input_check(accepted_values_range=[0, 1000]))
			break
		except ModelNotFoundError:
			print(f"Can not store model '{model}' since it was not found in equipment dictionary")
		except StorageOverflowError:
			print(f"Not enough room to store {command} of {model}")


def transfer_menu():
	print("-" * 30)
	print("Choose equipment to transfer:")
	i = 1
	for model, qty in w.count_by_model.items():
		info = OfficeEquipment.model_info_dict[model]
		print(f"{i}: {info.get('equipment_type').capitalize()} {info.get('brand')} {model}: {qty} unit{'s' if qty > 1 else ''}")
		i += 1

	command = input_check(accepted_values_range=[1, i-1])
	model = list(w.count_by_model.keys())[command - 1]
	try:
		print("How much you wish to transfer?")
		qty = input_check(accepted_values_range=[0, 1000])
		print("And to which department?")
		dep_list = list(department_dict.keys())
		i = 1
		for d in dep_list:
			print(f"{i}: {d}")
			i += 1
		dep = dep_list[input_check(accepted_values_range=[1, len(department_dict)])]
		w.transfer(model, dep, qty)
	except ModelNotFoundError:
		print(f"Can not find model '{model}' in warehouse!")
	except DepartmentNotFoundError:
		print(f"Department {dep} does not exist!")
	except NotEnoughEquipmentUnits:
		print(f"Can not transfer {qty} units of {model} to {dep} department since there's not enough units!")


department_dict = {
	'Sales': Department('Sales'),
	'Marketing': Department('Marketing'),
	'IT': Department('IT'),
	'HR': Department('HR'),
	'Accounting': Department('Accounting'),
	'Maintenance': Department('Maintenance')
}


w = Warehouse(25)

w.fill_random()

while True:

	print("-" * 30)
	print("<<< SUPER WAREHOUSE v0.1 >>>")
	print("Choose an option from the menu:\n")
	print("1. Show stored equipment list")
	print("2. Store equipment")
	print("3. Transfer items")
	print("\n0. Exit")

	command = input_check(accepted_values_range=[0, 4])

	if command == 1:
		stored_equipment_menu()
	elif command == 2:
		store_menu()
	elif command == 3:
		transfer_menu()
	elif command == 0:
		print("-" * 30)
		print("Exiting the program.")
		break
