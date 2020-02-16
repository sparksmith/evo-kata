def generate_trigrams(text):
    if len(text)<3:
        print("----> Text length too short.")
        exit()
    print("--> Generating Trigrams")
    # take word1 word2 word3 and add them as a list to a list 
    trigrams = lambda a: zip(a, a[1:], a[2:])

    # split the text into words
    text_tokens = text.split(' ')
    # run the lambda against the word list
    result = trigrams(text_tokens)

    #return it as list 
    return list(result)