class IncorrectDateFormatError(Exception):

	def __init__(self, msg):
		self.text = f"IncorrectDateFormatError: \n{msg}"


class Date:
	months_days_cnt_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
	month_names_dict = {
		1: 'Jan', 2: 'Feb', 3: 'Mar',
		4: 'Apr', 5: 'May', 6: 'Jun',
		7: 'Jul', 8: 'Aug', 9: 'Sep',
		10: 'Oct', 11: 'Nov', 12: 'Dec'
	}

	def __init__(self, date_str='01-01-1900'):
		self.day, self.month, self.year = self.parse_date_str(date_str)

	def __str__(self):
		return f"{self.day:02d}-{self.month:02d}-{self.year:04d}"

	@classmethod
	def make(cls, date_str: str):
		"""Returns new object from date_str if data is valid while handling exceptions."""
		try:
			return cls(date_str)
		except (ValueError, IncorrectDateFormatError) as err:
			print(f"Could not create Date object from data: '{date_str}'!\n\t{err}\n")

	@classmethod
	def parse_date_str(cls, date_str: str):
		"""Returns (day, month, year) from date_str if data is valid."""
		if date_str and type(date_str) == str and len(date_str) == 10:
			return cls.validate(int(date_str[0:2]), int(date_str[3:5]), int(date_str[6:10]))
		else:
			raise IncorrectDateFormatError(f"input must be a string of format 'DD-MM-YYYY'")

	@staticmethod
	def validate(dd: int, mm: int, yyyy: int):
		"""Validates and returns (day, month, year) from (dd, mm, yyyy) if there is such date."""
		if type(dd) == type(mm) == type(yyyy) == int:
			if mm in Date.months_days_cnt_dict.keys():
				days_in_month = Date.months_days_cnt_dict[mm] + (1 if not yyyy % 4 else 0)
				if 0 >= dd:
					raise IncorrectDateFormatError(f"day number must be above zero")
				elif dd > days_in_month:
					raise IncorrectDateFormatError(f"there are only {days_in_month} days"
												   f" in {Date.month_names_dict[mm]} of {yyyy}")
				else:
					return dd, mm, yyyy
			else:
				raise IncorrectDateFormatError(f"month can not be set to {mm}")
		else:
			raise TypeError(f"all arguments must be int")


# Bad data
Date.make(None)
Date.make(124)
Date.make('asd')
Date.make('1.-05-1978')
Date.make('20-13-2012')
Date.make('20-01-0')
Date.make('29-02-2001')
Date.make('00-05-1789')
Date.make('703-05-1789')

# Good data
# Using factory to handle errors
print(f"Date.make result: {Date.make('03-05-1989')}")
print(f"Date.make result: {Date.make('13-11-2002')}")
print(f"Date.make result: {Date.make('29-02-2000')}")

print(f"Date.parse_date_str result: {Date.parse_date_str('22-07-1978')}")
print(f"Date.parse_date_str result: {Date.parse_date_str('19-12-2015')}")

print(f"Date.validate result: {Date.validate(22, 10, 2019)}")
print(f"Date.validate result: {Date.validate(7, 1, 1999)}")
