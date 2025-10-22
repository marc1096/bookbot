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
def sorted_list(each_character_appears):
    def sort_on(rec): return rec["num"]
    results = []
    for ch, num in each_character_appears.items():
        if ch.isalpha():
            results.append({"char": ch, "num": num})
    results.sort(reverse=True, key=sort_on)
    return results
