def count_words(book):
    words = book.split()

    return len(words)


def count_chars(book):
    list_of_chars = list(book.lower())
    char_dict = {}

    for char in list_of_chars:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict