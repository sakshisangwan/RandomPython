# Finding letter in a string from a specified index

def find(word, letter, start):
	while start < len(word):
		if word[start] == letter:
			return start
		start = start + 1

	return -1

x = find ("hello my name is pypi", "m", 7)
print(x)