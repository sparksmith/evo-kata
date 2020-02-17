import unittest
import sys
sys.path.insert(0, '../modules/')

from trigram import *

class TestTrigram(unittest.TestCase):

	def test_generate_trigrams(self):
		test_data= "I wish I was"
		result_test= [("I", "wish", "I"), ("wish", "I", "was")]

		self.assertEqual(generate_trigrams(test_data), result_test, "Should have 2 trigrams")

if __name__ == "__main__":
    unittest.main()