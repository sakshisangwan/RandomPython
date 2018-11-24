def counter(word, letter, start):
	count = 0
	while start < len(word):
		if word[start] == letter:
			count = count + 1
		start = start + 1
	print(count)

counter('Hello hey hi qwerty say way dya may hay bay slay', 'a', 26)