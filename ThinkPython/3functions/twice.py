def do_twice(f,word):
	f(word)
	f(word)

def print_spam(word):
	print(word)

def print_twice(bruce):
	print(bruce)
	print(bruce)

def do_four(func, arg):
    do_twice(func, arg)
    do_twice(func, arg)


do_twice(print_twice, 'spam')
print('')

do_four(print_twice, 'spam')