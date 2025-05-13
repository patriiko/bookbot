from stats import count_words


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def main():
    book_path = "books/frankenstein.txt"

    book_txt = get_book_text(book_path)
    num_of_words = count_words(book_txt)

    print(f"{num_of_words} words found in the document")


main()