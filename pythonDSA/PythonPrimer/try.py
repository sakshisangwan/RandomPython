# temperature = 98.6
# original  = temperature
# temperature = temperature+ 5.0

# print(temperature)
# print(original)


# data = ['h', 'e', 'l', 'l', 'o']

# hello = 'hello'
# hello1 = list(hello)
# backup = list(hello1)


# print(hello)
# print(hello1)
# print(data)
# print(backup)

# reply = input('Enter x and y, separated by spaces: ')
# pieces = reply.split()


# x = float(pieces[0])
# y = float(pieces[1])

# print(pieces)
# print(x)
# print(y)

# age = int(input("Enter age"))

# max_heart_rate = 206.9 - (0.67 * age)
# target = 0.65 * max_heart_rate
# print('Your target', target)


# def sqrt(x):
# 	if not isinstance(x, (int, float)):
# 		raise TypeError('x must be numeric')
# 	elif x < 0:
# 		raise ValueError('x cannot be negative')


# y = sqrt('x')

n=100

factors = (k for k in range(1, n+1) if n%k == 0)
print(factors)