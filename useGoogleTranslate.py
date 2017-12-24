from googletrans import Translator
import random
import operator as op
import math
import sys
import itertools

def run():
    length = int(input("Length(-1 to quit): "))
    if length == -1 : sys.exit()
    translator = Translator()
    translateShuffleWord = []
    shuffleWord = []
    for i in itertools.permutations(inp, length):
        word = ''.join(i)
        shuffleWord.append(word)
        ab = translator.translate(word, src='en', dest='ja')
        translateShuffleWord.append(ab.text.upper())
        if word != ab.text.upper() :
            print(word,end=' ')
            print (ab.text.upper())
    o=0
    
    for i in shuffleWord:
        word = ''.join(i)
        if word != translateShuffleWord[o] :
            ans.append(word)
        o+=1
    for i in ans:
        print(i)
if __name__ == '__main__':
    inp = input("CHAR: ").upper()
    while True:
        run()
