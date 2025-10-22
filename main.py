from stats import count_words, count_chars, sorted_list
def get_book_text(frankenstein):
    with open(frankenstein) as f:
        return f.read()
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)


    word_count_result = count_words(text)
    char_counts_result=count_chars(text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count_result} total words")
    print("--------- Character Count -------")

    sorted_chars = sorted_list(char_counts_result)  # your stats function
    for item in sorted_chars:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()


