def check_fermat(a, b, c, n):
	if(n > 2 and a**n + b**n == c**n):
		print("Holy smokes, Fermat was wrong!")
	else:
		print("No that doesn't work")

def get_fermat_params():
	a = input("Enter a\n")
	b = input("Enter b\n")
	c = input("Enter c\n")
	n = input("Enter n\n")
	check_fermat(int(a), int(b), int(c), int(n))


get_fermat_params()