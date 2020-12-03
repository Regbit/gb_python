class AltZeroDivisionError(Exception):
	pass


def dividend():
	while True:
		try:
			return float(input("Enter dividend: "))
		except ValueError:
			print("Enter a VALID number!")


def divisor():
	while True:
		try:
			out = float(input("Enter divisor: "))
			if out:
				return out
			else:
				raise AltZeroDivisionError
		except ValueError:
			print("Enter a VALID number!")
		except AltZeroDivisionError:
			print("Divisor can not be zero!")


print(dividend() / divisor())
