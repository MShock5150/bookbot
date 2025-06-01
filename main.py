import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import (
        get_word_count, 
        get_letter_dict,
        sort_dict_to_list,
        )

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    book = sys.argv[1]
    text = get_book_text(book)
    word_count = get_word_count(text)
    letter_dict = get_letter_dict(text)
    sorted_letter_list = sort_dict_to_list(letter_dict)
    print_report(book, word_count, sorted_letter_list)

def print_report(book, word_count, sorted_letter_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for letter in sorted_letter_list:
        if not letter["char"].isalpha():
            continue
        print(f"{letter['char']}: {letter['num']}")
    
    print("============= END ===============")

main()
