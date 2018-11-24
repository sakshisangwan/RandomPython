def decorator_function(original_function):
	def wrapper_function(*args, **kwargs):
		print('wrapper executed this before {}'.format(original_function.__name__))
		return original_function(*args, **kwargs)
	return wrapper_function

# class DecoratorClass(object):

# 	def __init__(self, original_function):
# 		self.original_function = original_function

# 	def __call__(self, *args, **kwargs):
# 		print('call method executed this before {}'. format(self.original_function.__name__))
# 		return self.original_function(*args, **kwargs)
		

# @DecoratorClass
# def display():
# 	print('decorator function')

# @DecoratorClass
# def display_info(name, age):
# 	print('display_info ran with arguments ({0}, {1})'. format(name, age))

@decorator_function
def display():
	print('decorator function')

@decorator_function
def display_info(name, age):
	print('display_info ran with arguments ({0}, {1})'. format(name, age))

display_info('John', 23)
display()