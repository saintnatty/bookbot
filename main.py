import sys
from stats import get_num_words, get_char_amounts, sort_on

def main():
#    book_path = "books/frankenstein.txt"
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters_dictionary = get_char_amounts(text)
    is_sorted = sort_on(characters_dictionary)
#    print(f"Found {num_words} total words")
#    print(characters_dictionary)
#    sort_on(characters_dictionary)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_count in is_sorted:
        if char_count['char'].isalpha():
            print(f"{char_count['char']}: {char_count['num']}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

if len(sys.argv) < 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()