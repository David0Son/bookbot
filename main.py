import sys
from stats import *

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    #book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    print("--------- Character Count -------")
    num_chars = get_num_chars(text)
    dict_list = create_sorted_list_of_dicts(num_chars)
    for letter in dict_list:
        for key, value in letter.items():
            print(f"{key}: {value}")
    #print(dict_list)
    print("============= END ===============")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        #print(path_to_file)
        file_contents = f.read()
    return file_contents

main()