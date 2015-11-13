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
    puzzle= list("*" * length)
    # print puzzle[1]
    # print puzzle
    mistakes=0
    max_mistakes=10
    while mistakes < max_mistakes :
        print ''.join(puzzle)
        print "Used {} :: Missed : {}".format(used,mistakes)
        print "Enter a letter : ",
        option = raw_input()
        used.append(option)
        hit = -1
        while secret_word.find(option, hit + 1) != -1 :
            hit = secret_word.find(option, hit + 1)
            puzzle[hit] = secret_word[hit]
        if hit == -1 :
            print "Incorrect"
            mistakes += 1
        else :
            print "Good"
        if '*' not in puzzle :
            print "Congragulations!! You found the word %r" % secret_word
            break
        elif mistakes == max_mistakes :
            print "You lose!! The word is %r" % secret_word
            break
    
wordlist = get_wordlist()
secret = select_word(wordlist)
play_hangman(secret)
