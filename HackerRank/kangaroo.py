def jump(x1, v1, x2, v2):
	if 0 <= x1 <= 10000 and 0 <= x2 <= 10000 and 1 <= v1 <= 10000 and 1 <= v2 <= 10000:
		if x2 < x1 and v2 < v1:
			print('NO')
		elif (((x1-x2)<=0 and (v2-v1)<0) and (x1-x2)%(v2-v1) == 0) or (((x1-x2)>=0 and (v2-v1)>0) and (x1-x2)%(v2-v1) == 0):
			print('YES')
		else:
			print('NO')
	else:
		print('NO')

def main():
	z = input().split()
	list(set(z))
	map(int, z)
	jump(int(z[0]), int(z[1]), int(z[2]), int(z[3]))


if __name__ == '__main__':
    main()