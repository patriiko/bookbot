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


def sort_on(dict):
    return dict["num"]


def sort_dict(dict):
    chars_list = []

    for char, count in dict.items():
        char_info = {"char": char, "num": count}
        chars_list.append(char_info)

    chars_list.sort(reverse=True, key=sort_on)

    return chars_list