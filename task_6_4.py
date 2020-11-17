class Car:
	_speed = 0
	_color = None
	_name = ''
	_is_police = False

	def __init__(self, speed, color, name, is_police):
		self._speed = speed
		self._color = color
		self._name = name
		self._is_police = is_police

	def go(self, speed):
		self._speed = speed
		print(f"{self._name}: moving")

	def stop(self):
		self._speed = 0
		print(f"{self._name}: stopping")

	def turn(self, direction):
		print(f"{self._name}: turning {direction}.")

	def show_speed(self):
		print(f"{self._name}: speed = {self._speed} km/h")


class TownCar(Car):

	def __init__(self, speed, color, name):
		super().__init__(speed, color, name, 0)

	def show_speed(self):
		super().show_speed()
		if self._speed > 60:
			print("WARNING: Town car can't go faster that 60 km/h!")


class SportCar(Car):

	def __init__(self, speed, color, name):
		super().__init__(speed, color, name, 0)


class WorkCar(Car):

	def __init__(self, speed, color, name):
		super().__init__(speed, color, name, 0)

	def show_speed(self):
		super().show_speed()
		if self._speed > 40:
			print("WARNING: Work car can't go faster that 40 km/h!")


class PoliceCar(Car):

	def __init__(self, speed, color, name):
		super().__init__(speed, color, name, 1)


town_car = TownCar(0, 'Brown', 'Town car')
town_car.go(75)
town_car.show_speed()

sport_car = SportCar(0, 'Red', 'Sport car')
sport_car.go(140)
sport_car.show_speed()

work_car = WorkCar(0, 'Yellow', 'Work car')
work_car.go(45)
work_car.show_speed()

police_car = PoliceCar(0, 'Blue', 'Police car')
police_car.go(60)
police_car.show_speed()
