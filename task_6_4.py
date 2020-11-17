class Car:
	speed = 0
	color = None
	name = ''
	is_police = False

	def __init__(self, speed, color, name, is_police):
		self.speed = speed
		self.color = color
		self.name = name
		self.is_police = is_police

	def go(self):
		print("Car is moving")

	def stop(self):
		print("Car is stopping")

	def turn(self, direction):
		print(f"Car is turning {direction}")


class TownCar(Car):
	pass

