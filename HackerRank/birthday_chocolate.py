def birthday(s, d, m):
	i = 0
	count = 0
	while i <= len(s)-m:
		sum = 0
		for j in range(m):
			sum += int(s[i+j])
		if sum == d:
			count +=1
		i += 1
	return count

def main():
	num = input()
	s = input().split()
	list(set(s))
	dob = input().split()
	list(set(dob))

	print(birthday(s, int(dob[0]), int(dob[1])))

if __name__ == '__main__':
	main()