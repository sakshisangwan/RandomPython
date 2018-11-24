def is_triangle(side1, side2, side3):
	if(side1 + side2 == side3 or side1 + side3 == side2 or side2 + side3 ==side1):
		print("Yes")
	else:
		print("No")

def stick_length():
	side1 = input("Enter length of 1st stick\n")
	side2 = input("Enter length of 2nd stick\n")
	side3 = input("Enter length of 3rd stick\n")
	is_triangle(int(side1), int(side2), int(side3))

stick_length()