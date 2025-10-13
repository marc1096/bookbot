from stats import count_words
def get_book_text(frankenstein):
    with open(frankenstein) as f:
        return f.read()
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    result = count_words(text)
    print(f"Found {result} total words")

main()

