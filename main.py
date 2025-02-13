def main():
    with open("books/frankenstein.txt", "r", encoding="utf-8") as f:
        file_contents = f.read()
        
        # Count words and characters
        word_count = countWords(file_contents)
        char_count = countChars(file_contents)
        
        # Print report
        printReport(word_count, char_count)

def countWords(text):
    words = text.split()
    return len(words)

def countChars(text):
    """Counts occurrences of each alphabetical character in the text."""
    text = text.lower()
    char_dict = {}
    
    for char in text:
        if char.isalpha():  # Only count alphabetic characters
            char_dict[char] = char_dict.get(char, 0) + 1

    return char_dict

def printReport(word_count, char_dict):
    """Prints a formatted report of word and character frequency."""
    print("--- Begin report of frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    sorted_char = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_char:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()