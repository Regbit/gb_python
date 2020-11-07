def int_func(lowercase_word):
	"""Takes a lower cased latin word and capitalizes it."""
	if max(lowercase_word) <= 'z' and min(lowercase_word) >= 'a':
		return lowercase_word.capitalize()


print(int_func('someword'))

new_line = 'nice авп ъghj jапро hjjпаро вапрghgh cool Asdf 34g2d' # input("")
out = []

for word in new_line.strip().split():
	res = int_func(word)
	if res:
		out.append(res)

print(out)
