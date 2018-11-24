# eng2sp = {'one':'uno', 'two':'dos', 'three':'tres'}
# print('one' in eng2sp)

# vals = eng2sp.values()
# print('uno' in vals)

def histogram(s):
	d = dict()
	for c in s:
		d[c] = d.get(c, 0) + 1
	return d

def print_hist(h):
	for c in h:
		print(c, h[c])

def reverse_lookup(h, v):
	for c in h:
		if h[c] == v:
			return c
	raise LookupError()

def invert_dict(d):
	inverse = dict()
	for key in d:
		val = d[key]
		if val not in inverse:
			inverse[val] = [key]
		else:
			inverse[val].append(key)
	return inverse


h = histogram('hello')
print(invert_dict(h))

# print(reverse_lookup(h, 2))