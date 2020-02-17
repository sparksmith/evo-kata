import unittest
import sys
sys.path.insert(0, '../modules/')

from generator import *

class TestGenerator(unittest.TestCase):

	def test_first_word_one_option(self):
		test_data = [("I", "wish", "I")]
		result_data = ["I", "wish", "I"]

		running_result = get_first_words(test_data)

		self.assertEqual(running_result,result_data, "Should be the test data.")


	def test_first_word_more_option(self):
		test_data = [("1", "wish1", "I1"),("2", "wish2", "I2"),("3", "wish3", "I3")]

		running_result = tuple(get_first_words(test_data))

		self.assertEqual(running_result in test_data,True, "Should exist in the list.")


	def test_generate_test(self):
		test_data = [("I", "wish", "I")]
		result_data = "I wish I"
		test_length = 10

		running_result = generate_text(test_data, test_length)

		self.assertEqual(running_result, result_data, "Should be 'I wish I'")


	def test_recursive_generation(self):
		test_data = [("I", "wish", "I"), ("wish", "I", "might")]
		test_length = 10
		result_data = ["I", "do", "I", "wish", "I", "might"]

		running_result = recursive_generation(test_data, ["I", "do", "I", "wish"], test_length)

		self.assertEqual(running_result, result_data, "Should be 'I do I wish I might'")


if __name__ == "__main__":
    unittest.main()