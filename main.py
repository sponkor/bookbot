def main():
    with open("./books/frankenstein.txt") as f:
        bookContents = f.read()
        #print(bookContents)
        print(wordCount(bookContents))

def wordCount(text):
    totalCount = []
    totalCount = text.split()
    return len(totalCount)
        
main()