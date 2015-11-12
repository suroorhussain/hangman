import random

def get_wordlist() :
    f=open("/usr/share/dict/words")
    clean_words = []
    for i in f :
        i = i.strip()
        if i.isalpha() and len(i) >5 :
            clean_words.append(i.lower())
    return clean_words

def select_word(wordlist) :
    return random.sample(wordlist, 1)[0]

def play_hangman(secret_word) :
    length=len(secret_word)
    used = []
    puzzle= "*" * length
    mistakes=0
    max_mistakes=10
    while mistakes < max_mistakes :
        print puzzle
        print "Used {} :: Missed : {}".format(used,mistakes)
        print "Enter a letter : ",
        option=raw_input()
        hit=0
        search = secret_word.find(option)
        if search != -1 :
            
            
        
    
wordlist = get_wordlist()
secret = select_word(wordlist)
play_hangman(secret)
