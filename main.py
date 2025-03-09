import sys
from stats import get_num_words, get_num_char, print_char_list

def main():
    # book_path = "books/frankenstein.txt"
    book_path = ''
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = str(sys.argv[1])
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_char(text)
    # print(text)  # L3: Read file
    # print(f"{num_words} words found in the document")  # LL4 & 5: Count words & Refactor
    # print(num_chars)  # L6: Count Characters

    #####/////  Book Word/Char Count Report  /////#####

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print_char_list(num_chars)
    print("============= END ===============")



def get_book_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        # text = f.read()
        # text = text.replace('ſ', 's')
        # return text
        return f.read()
    




if __name__ == '__main__':
    main()

