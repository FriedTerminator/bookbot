def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = countChars(file_contents)
    print(words)

def countChars(text):
    text = text.lower()
    thisdict = {}
    for char in text:
        if(char in thisdict):
            thisdict[char] += 1
        else: 
            thisdict[char] = 1
    return thisdict

if __name__ == "__main__":
    main()