# fin = open('words.txt')
# for line in fin:
# 	word = line.strip()
# 	if len(word) > 20:
# 		print(word)


def has_no_e():
	fin = open('words.txt')
	count = 0
	no_e_count = 0
	for line in fin:
		count = count + 1
		if not 'e' in line:
			print(line.strip())
			no_e_count = no_e_count + 1

	print((no_e_count/count) * 100)


has_no_e()