class Road:

	def __init__(self, length_m=0, width_m=0):
		self._length_m = length_m
		self._width_m = width_m

	def calc_asphalt_mass(self, height_sm=1, kg_per_square_meter_per_sm=25):
		return self._length_m * self._width_m * height_sm * kg_per_square_meter_per_sm


road_1 = Road(6500, 30)
print(f"To make the road you will need {road_1.calc_asphalt_mass(6, 27) / 1000} tons of asphalt.")

road_2 = Road(10300, 25)
print(f"To make the road you will need {road_2.calc_asphalt_mass(4, 23) / 1000} tons of asphalt.")
