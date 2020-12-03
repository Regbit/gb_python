class Complex:

	def __init__(self, real=0.0, imaginary=0.0):
		self.real = real
		self.imaginary = imaginary

	def __str__(self):
		return f"{self.real}{'+' if self.imaginary > 0 else ''}{self.imaginary}i"

	def add_sub(self, other, mul=1):
		real_res = self.real + mul * other.real
		imaginary_res = self.imaginary + mul * other.imaginary
		if real_res:
			if imaginary_res:
				return Complex(real_res, imaginary_res)
		return real_res

	def __add__(self, other):
		return self.add_sub(other)

	def __sub__(self, other):
		return self.add_sub(other, -1)

	def __mul__(self, other):
		# (a + bi) · (c + di) = (ac – bd) + (ad + bc)i
		return Complex(self.real * other.real - self.imaginary * other.imaginary,
					   self.real * other.imaginary + self.imaginary * other.real)


c1 = Complex(3, 15)
c2 = Complex(14, -7)
c3 = Complex(2, -15)
print(c1)
print(c2)
print(c1+c2, complex(3, 15) + complex(14, -7))
print(c1+c3, complex(3, 15) + complex(2, -15))
print(c1-c1, complex(3, 15) - complex(3, 15))
print(c1*c3, complex(3, 15) * complex(2, -15))
