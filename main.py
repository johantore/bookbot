import sys

from stats import (
    number_of_words,
    char_count,
    char_sort,
    file_read
)

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    file_path = sys.argv[1]
    text = file_read(file_path)
    word_count = number_of_words(text)
    char_dict = char_count(text)
    char_list_sorted = char_sort(char_dict)
    print_report(file_path, word_count, char_list_sorted)

def print_report(file_path, word_count, char_list_sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in char_list_sorted:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
