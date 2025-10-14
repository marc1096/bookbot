from stats import count_words
from stats import count_chars
def get_book_text(frankenstein):
    with open(frankenstein) as f:
        return f.read()
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count_result = count_words(text)
    char_counts_result=count_chars(text)
    print(f"Found {word_count_result} total words")
    print(char_counts_result)

main()


