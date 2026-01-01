from stats import number_of_words, char_count

def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    word_count = number_of_words(text)
    print(f"Found {word_count} total words")
    print(char_count(text))

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

main()
