class CreditCard:
	def __init__(self, customer, bank, acnt, limit):
		self._customer = customer
		self._bank = bank
		self._account = acnt
		self._limit = limit
		self._balance = 0

	def get_customer(self):
		return self._customer

	def get_bank(self):
		return self._bank

	def get_account(self):
		return self._account

	def get_limit(self):
		return self._limit

	def get_balance(self):
		return self._balance

	def charge(self, price):
		if price + self._balance > self._limit:
			return False
		else:
			self._balance += price
			return True

	def make_payment(self,amount):
		self._balance -= amount


# cc = CreditCard('John Doe', '1stBank', '2345 6789 2134 7654', 1000)

# print(cc.get_customer())

# cc1 = CreditCard('John', '1stBank', '2345 6789 2134 7654', 1000)

# print(cc1.get_customer())

# cc1.charge(200)
# print(cc1.get_balance())
# print(cc.get_balance())

if __name__ == '__main__':
	wallet = []
	wallet.append(CreditCard('John Doe', '1st Bank', '2345 6789 2134 7654', 2500))
	wallet.append(CreditCard('John Doe', '2nd Bank', '1234 6789 2134 7654', 3500))
	wallet.append(CreditCard('John Doe', '3rd Bank', '1345 6789 2134 7654', 5000))

for val in range(1, 17):
	wallet[0].charge(val)
	wallet[0].charge(2*val)
	wallet[0].charge(3*val)

for c in range(3):
	print('Customer = ', wallet[c].get_customer())
	print('Bank = ', wallet[c].get_bank())
	print('Account = ', wallet[c].get_account())
	print('Limit = ', wallet[c].get_limit())
	print('Balance = ', wallet[c].get_balance())
	while wallet[c].get_balance() > 100:
		wallet[c].make_payment(100)
		print('New Balance = ', wallet[c].get_balance())
	print()