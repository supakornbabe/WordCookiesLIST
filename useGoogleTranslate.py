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
    ans = []
    for i in itertools.permutations(inp, length):
        word = ''.join(i)
        shuffleWord.append(word)
        ab = translator.translate(word, src='en', dest='ja')
        translateShuffleWord.append(ab.text.upper())
        if word != ab.text.upper() :
            ans.append(word)
    ansSet = list(set(ans))
    ansSet.sort()
    for i in ansSet:
        print(i)
if __name__ == '__main__':
    inp = input("CHAR: ").upper()
    while True:
        run()
