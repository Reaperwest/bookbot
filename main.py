
def count_words(text):
    return len(text.split())

def count_alphabet_characters(text):
    char_count = {}

    for char in text.lower():  
        if char.isalpha():  
            char_count[char] = char_count.get(char, 0) + 1

    return char_count

def sort_on(char_dict):
    return char_dict["num"]

def generate_report(file_path, word_count, character_counts):
    print(f"--- Begin report of {file_path} ---\n")
    print(f"{word_count} words found in the document\n")

    char_list = [{"char": char, "num": count} for char, count in character_counts.items()]

    char_list.sort(reverse=True, key=sort_on)

    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("\n--- End report ---")

def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file, "r", encoding="utf-8") as f:
        file_contents = f.read()

    word_count = count_words(file_contents)

    character_counts = count_alphabet_characters(file_contents)

    generate_report(path_to_file, word_count, character_counts)

main()
