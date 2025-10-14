def count_words(text):
    word_count = text.split()
    number_of_words = len(word_count)
    return number_of_words

def count_chars(text):
    each_character_appears = {}
    for character in text:
        lowercased_character = character.lower()
        if lowercased_character in each_character_appears:
            each_character_appears[lowercased_character] += 1
        else: each_character_appears[lowercased_character] = 1
    return each_character_appears