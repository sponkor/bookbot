def main():
    with open("./books/frankenstein.txt") as f:
        bookContents = f.read()
        print(bookContents)
        
main()