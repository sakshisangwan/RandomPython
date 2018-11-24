prefixes = 'JKLMNOPQ'
suffix = 'ack'
suffix1 = 'uack'

for letter in prefixes:
	if letter == 'O' or letter == 'Q':
		print(letter+suffix1)
	else:
		print(letter+suffix)