from googletrans import Translator
import random
import operator as op
import math
import sys

def ncr(n, r):
    r = min(r, n - r)
    if r == 0:
        return 1
    numer = reduce(op.mul, xrange(n, n - r, -1))
    denom = reduce(op.mul, xrange(1, r + 1))
    return numer // denom

def run():
    length = int(input("Length(-1 to quit): "))
    if length == -1 : sys.exit()
    translator = Translator()
    noOfOutput = math.factorial(lenInp) / math.factorial(lenInp - length)
    no = 0
    shuffleWord = []
    while True:
        if no == noOfOutput:
            break
        has = False
        ran = ''.join(random.sample(inp, length))
        for i in shuffleWord:
            if ran == i:
                has = True
        if not has:
            shuffleWord.append(ran)
            no += 1
    #print(shuffleWord)
    translateShuffleWord = []
    for i in shuffleWord:
        ab = translator.translate(i, src='en', dest='ja')
        translateShuffleWord.append(ab.text.upper())
    for i in range(len(translateShuffleWord)):
        #print(shuffleWord[i], end='')
        #print(end=' ')
        #print(translateShuffleWord[i])
        if(translateShuffleWord[i] != shuffleWord[i]):
            print(shuffleWord[i])

if __name__ == '__main__':
    inp = input("CHAR: ")
    inp = inp.upper()
    lenInp = len(inp)
    while True:
        run()
