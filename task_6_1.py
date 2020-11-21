from itertools import cycle
import time


class TrafficLight:

	def __init__(self, red_sec=0, yellow_sec=0, green_sec=0):
		self.__color = None
		self.set_timing(red_sec, yellow_sec, green_sec)

	def set_timing(self, red_sec=0, yellow_sec=0, green_sec=0):
		timing_list = ['Red' for _ in range(red_sec)] + \
					  ['Yellow' for _ in range(yellow_sec)] + \
					  ['Green' for _ in range(green_sec)] + \
					  ['Yellow' for _ in range(yellow_sec)]

		self.__color = cycle(timing_list)

	def running(self):
		return next(self.__color)


traffic_light = TrafficLight(7, 2, 5)

sec = 0
while True:
	print(f"\r{sec//60:02d}:{sec%60:02d} {traffic_light.running()}", end='')
	time.sleep(1)
	sec += 1

