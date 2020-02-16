import random


def get_first_words(trigrams):
    print("---> Pick arbitrary starting point")
    list_size = len(trigrams)-1
    random_starting_point = random.randint(0, list_size)
    first_words = trigrams[random_starting_point]

    return list(first_words)


def generate_text(trigrams, max_length):
    print("--> Generating text based on trigrams")
    result = get_first_words(trigrams)

    result = recursive_generation(trigrams, result, max_length)

    return " ".join(result)


def recursive_generation(trigrams, current_text, max_length):
    current_text_size = len(current_text)
    # if the max length has been reached
    if max_length <= current_text_size:
        print("----> Maximum length reached.")
        return current_text

    # if the texts starting point is broken -> stop
    if current_text_size < 2:
        print("----> Initial text length must be bigger than 2 words.")
        return current_text

    # print("---> Adding word to text ",current_text)
    # get the last 2 words in the text
    keyword1 = current_text[current_text_size-2]
    keyword2 = current_text[current_text_size-1]

    # identify next word
    potential_next_word = [
        triple for triple in trigrams
        if keyword1 == triple[0] and keyword2 == triple[1]
    ]

    # if there is no next word exit
    if len(potential_next_word) < 1:
        print("----> No chain available ")
        return current_text

    # if there is more than 1 option -> choose at random
    option = 0
    if len(potential_next_word) > 1:
        option = random.randint(0, len(potential_next_word)-1)

    # if there is a potential next word -> add the new word -> call me again
    current_text.append(potential_next_word[option][2])
    recursive_generation(trigrams, current_text, max_length)

    # in Python a function that does not return enything returns a NoneType !
    return current_text
