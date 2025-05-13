from stats import count_words, count_chars, sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    book_txt = get_book_text(book_path)
    num_of_words = count_words(book_txt)
    chars_dict = count_chars(book_txt)
    sorted_chars_list = sort_dict(chars_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_chars_list:
        character = dict["char"]
        count = dict["num"]

        if character.isalpha():
            print(f"{character}: {count}")
    print("============= END ===============")


main()