def main():
    with open("./books/frankenstein.txt") as f: #opens the file and assigns it to 'f'
        bookContents = f.read() #formats the variable into a string and assigns it to 'bookContents'
        print(letterCount(wordCount(bookContents)))

def wordCount(text): #takes the contents of the text and returns the total number of words
    return text.split()

def letterCount(wordList): #takes a list of words and returns the count of each letter
    allLetters, listIndex, value = [], {}, 0 #declaring variables that get manipulated by the function
    for i in range(0, len(wordList)): 
        splitChar = list(wordList[i].lower()) #takes each word, makes it lowercase and splits the word into a list
        for letter in splitChar: #takes each character in a word and passes it to the 'if' function below which tests if each character is a letter and if it's been indexed 
            if letter.isalpha() == True and letter in listIndex: #if the letter has already been indexed the "count" associated with the character is increased
                allLetters[listIndex[letter]]["count"] += 1
            elif letter.isalpha() and letter not in listIndex: #if the letter hasn't been indexed, it is added and given a value and appended the list of characters and their counts
                listIndex[letter] = value
                value += 1
                allLetters.append({"letter": letter, "count": 1})
    return allLetters
main()