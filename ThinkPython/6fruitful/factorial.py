def factorial(num):
	if(num == 0):
		return 1
	else:
		recurse = factorial(num - 1)
		result = num * recurse
		return result

print(factorial(3))