from stats import count_words, count_chars


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def main():
    book_path = "books/frankenstein.txt"

    book_txt = get_book_text(book_path)
    num_of_words = count_words(book_txt)
    num_of_chars = count_chars(book_txt)

    print(f"{num_of_words} words found in the document")
    print(num_of_chars)


main()