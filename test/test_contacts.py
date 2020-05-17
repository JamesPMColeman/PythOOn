import unittest
from program.contacts import Address


class TestAddress(unittest.TestCase):

	def test_address(self):
		street = '234 First st.'
		city = 'Everytown'
		state = 'AA'
		zipcode = '123456'
		address = Address(street, city, state, zipcode)

		result = address.__str__()
		self.assertEqual(result, 
			street + '\n' + city + ', ' + state + ' ' + zipcode)

	def test_address_with_second_street(self):
		street = '234 First st.'
		city = 'Everytown'
		state = 'AA'
		zipcode = '123456'
		street_2 = 'Apple'
		address = Address(street, city, state, zipcode, street_2)

		result = address.__str__()
		self.assertEqual(result, 
			street + '\n' + street_2 + '\n' + city + ', ' + state + ' ' + zipcode)
