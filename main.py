def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letters = get_characters(text)
    letters_dictionary = list_of_characters(letters)

    letters_dictionary.sort(key=lambda x: x['num'], reverse=True)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()

    for char_pair in letters_dictionary:
        print(f"The '{char_pair['char']}' character was found {char_pair['num']} times")

    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_characters(text):
    all_freq = {}
    lower_text = text.lower()
    for i in lower_text:
        if i.isalpha():
            if i in all_freq:
                all_freq[i] += 1
            else:
                all_freq[i] = 1
    return all_freq

def list_of_characters(characters):
    char_list = []
    for char, count in characters.items():
        dictionary = {"char": char, "num": count}
        char_list.append(dictionary)
    return(char_list)

main()