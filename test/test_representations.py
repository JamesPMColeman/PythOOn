import unittest
from program.representations import DictionaryMixin


class TestDictionaryMixin(unittest.TestCase):
	
	class test_class(DictionaryMixin):

		@property
		def property(self):
			return "I am a property"

		_test_attr = ''


	def test_to_dict(self):
		test_test_class = self.test_class()
		result = test_test_class.to_dict()
		self.assertIsNotNone(result)

	def test__represent(self):
		test_test_class = self.test_class()
		result = test_test_class._represent(test_test_class)
		self.assertEqual(result, {})