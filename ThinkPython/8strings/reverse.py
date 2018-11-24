def reverse(str):
	index = len(str) - 1
	while index >= 0:
		letter = str[index]
		print(letter)
		index = index - 1

reverse('hello')