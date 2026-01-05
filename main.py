from stats import (
    number_of_words, 
    char_count, 
    char_sort
)

def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    word_count = number_of_words(text)
    char_dict = char_count(text)
    char_list_sorted = char_sort(char_dict)
    print_report(file_path, word_count, char_list_sorted)

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

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
