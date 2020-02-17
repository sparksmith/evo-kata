import sys
sys.path.insert(0, '../modules/')

from trigram import *

def test_generate_trigrams():
	test_data= "I wish I was"
	result_test= [("I", "wish", "I"), ("wish", "I", "was")]

	assert generate_trigrams(test_data) == result_test

if __name__ == "__main__":
    test_generate_trigrams()
    print("Everything passed")