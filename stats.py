# count the words in a book
def count_words(text):
    text = text.split()
    return len(text)

# count the characters in a book
def count_characters(text):
    char_dict = {}
    for char in text.lower():
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

# sort the characters by frequency
def sort_characters(char_dict):
    return sorted(char_dict.items(), key=lambda x: x[1], reverse=True)