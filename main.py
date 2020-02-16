# Kata 14
# Main File

# common imports
import re

# custom imports
from modules.file_handling import *
from modules.generator import *
from modules.trigram import *

# settings 
BASE_BOOK = "assets/simple.txt"
RESULT_BOOK = "result.txt"
TEXT_LENGTH = 100

############################################################################

def main():
    print("-> Start App")
    # Read the book
    result = readFile(BASE_BOOK)
    # make the text all lower case
    result = result.lower() 
    # remove punctuation 
    result = re.sub(r'[^a-zA-Z0-9\s]', '', result)
    # generate trigrams 
    trigrams = generate_trigrams(result)
    # generate text based on trigrams
    generated = generate_text(trigrams)
    writeResult(RESULT_BOOK, generated)
    

if __name__ == '__main__':
    main()