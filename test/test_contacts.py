import unittest
from program.contacts import Address, _AddressBook 


class TestAddress(unittest.TestCase):

	book = _AddressBook()

	def test_get_address(self):
		result = self.book.get_address(1)
		self.assertTrue(isinstance(result, Address))

	def test_get_address_with_bad_imput(self):
		with self.assertRaises(ValueError):
			self.book.get_address(0)

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
