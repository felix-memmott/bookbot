import sys
from stats import count_words, count_characters, sort_characters

# get the text of a book from a filepath
def get_book_text(filepath):
    with open(filepath, "r") as file:
        return file.read()

# main function
def main():
    # check if the user has provided a filepath
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    text = get_book_text(sys.argv[1])
    print("----------- Word Count ----------")
    word_count = count_words(text)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_dict = count_characters(text)
    sorted_chars = sort_characters(char_dict)
    for char, count in sorted_chars:
        print(f"{char}: {count}")
    print("============= END ==============")

main()
