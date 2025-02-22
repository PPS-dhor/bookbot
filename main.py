def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_char(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print(' ')
    print_char_list(num_chars)
    print("--- End report ---")

def get_book_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        # text = f.read()
        # text = text.replace('ſ', 's')
        # return text
        return f.read()


def get_num_words(text):
    # words = text.split()
    # return len(words)
    return len(text.split())


def get_num_char(text):
    char_dict = {}

    # chars = list(text)
    # for char in chars:
    #     if char.isupper():
    #         lower_char = char.lower()
    #         if lower_char in char_dict:
    #             char_dict[lower_char] += 1
    #         else:
    #             char_dict[lower_char] = 1
    #     else:
    #         if char in char_dict:
    #             char_dict[char] += 1
    #         else:
    #             char_dict[char] = 1

    for char in text:
        # Convert uppercase letters to lowercase
        key = char.lower() if char.isupper() else char
        char_dict[key] = char_dict.get(key, 0) + 1
    return char_dict


def print_char_list(char_dict):
    # sorted_tuples = sorted(char_dict.items(), key=lambda item: item[1])
    # sorted_tuples.reverse()
    # for tup in sorted_tuples:
    #     if tup[0].isalpha():
            # print(...)
    sorted_tuples = sorted(char_dict.items(), key=lambda item: item[1], reverse=True)
    for char, count in sorted_tuples:
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")


if __name__ == '__main__':
    main()

