def main():
    with open("./books/frankenstein.txt") as f:
        bookContents = f.read()
        #print(bookContents) prints the entirety of the text
        #print(wordCount(bookContents)) prints the total word count
        print(letterCount(bookContents))

def wordCount(text):
    totalCount = []
    totalCount = text.split()
    return len(totalCount)

def letterCount(wordList):
    allCharacters = {}
    for item in wordList:
        character = item.split()
        for letter in character:
            lowercase = letter.lower()
            if lowercase.isalpha() == True and lowercase in allCharacters:
                allCharacters[lowercase] += 1
            elif lowercase.isalpha() and lowercase not in allCharacters:
                allCharacters[lowercase] = 1
    return allCharacters
main()