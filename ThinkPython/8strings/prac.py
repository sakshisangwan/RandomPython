def any_lowercase1(s):
	for c in s:
		if not c.islower():
			return False
	return True


print(any_lowercase1('hello'))