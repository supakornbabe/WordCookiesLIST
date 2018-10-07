import operator as op
import math
import random
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
    if length == -1 :
        sys.exit()
    noOfOutput = math.factorial(lenInp) / math.factorial(lenInp - length)/noOfSame 
    no = 0
    shuffleWord = []
    f = open('word.txt', 'r')
    lines = [item.strip().upper() for item in f.readlines()]
    while True:
        if no == noOfOutput:
            break
        has = False
        print(no,end=' ')
        print(noOfOutput)
        ran = ''.join(random.sample(inp, length))
        for i in shuffleWord:
            if ran == i:
                has = True
        if not has:
            shuffleWord.append(ran.upper())
            no += 1
    ans = []
    print(shuffleWord)
    print(len(shuffleWord))
    for i in shuffleWord:
        for line in lines:
            if i == line:
                ans.append(i)
    ans.sort()
    for i in ans:
        print (i)

if __name__ == '__main__':
    inp = input("CHAR: ")
    inp = inp.upper()
    lenInp = len(inp)
    noOfSame = int(input("Same: "))
    while True:
        run()
        