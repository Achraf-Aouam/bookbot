from stats import get_number_words, count_characters

import sys

def main():
    if len( sys.argv) < 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    print("============ BOOKBOT ============ \nAnalyzing book found at "+filepath+"...\n----------- Word Count ----------")
    print("Found "+str(get_number_words(filepath)) + " total words")
    print("--------- Character Count -------")
    mem = count_characters(filepath)
    for k , v in mem:
        if(k.isalpha()):
            print(k + ': '+str(v))
    print ("============= END ===============")



main()