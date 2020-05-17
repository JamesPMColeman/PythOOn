class Address:

	def __init__(self, street, city, state, zipcode, street2=''):
		self.street = street
		self.street2 = street2
		self.city = city
		self.state = state
		self.zipcode = zipcode

	def __str__(self):
		address = [self.street]
		if self.street2:
			address.append(self.street2)
		address.append(f'{self.city}, {self.state} {self.zipcode}')
		return '\n'.join(address)
