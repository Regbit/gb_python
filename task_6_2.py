class Road:

	_length = 0
	_width = 0

	def __init__(self, length=0, width=0):
		self._length = length
		self._width = width

	def calc_asphalt_mass(self, height=1, mass_per_square_meter=25):
		return self._length * self._width * height * mass_per_square_meter


road_1 = Road(6500, 30)
print(f"To make the road you will need {road_1.calc_asphalt_mass(6, 27) / 1000} tons of asphalt.")

road_2 = Road(10300, 25)
print(f"To make the road you will need {road_2.calc_asphalt_mass(4, 23) / 1000} tons of asphalt.")
