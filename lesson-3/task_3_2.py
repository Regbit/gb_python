def user_data(first_name='N/A', last_name='N/A', birth_year=1900, city='N/A', email='N/A', phone='N/A'):
	return f"User data: " \
		   f"first_name = {first_name}; " \
		   f"last_name = {last_name}; " \
		   f"birth_year = {birth_year}; " \
		   f"city = {city}; " \
		   f"email = {email}; " \
		   f"phone = {phone}"


kwargs = {
	'birth_year': 1990,
	'email': 'mail@email.ru',
	'first_name': 'Ivan',
	'city': 'Moscow',
	'phone': '+7(900)000-00-00',
	'last_name': 'Ivanov'
}

print(user_data(**kwargs))
