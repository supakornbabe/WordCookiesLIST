import itertools
import math
import sys
def run():
    length = int(input("Length(-1 to quit): "))
    if length == -1 :
        sys.exit()
    ans=[]
    for i in itertools.permutations(inp, length):
        word = ''.join(i)
        for line in lines:
            if line == word:
                ans.append(word)
    ansSet = list(set(ans))
    ansSet.sort()
    for i in ansSet:
        print(i)

if __name__ == '__main__':
    f = open('word.txt', 'r')
    lines = [item.strip().upper() for item in f.readlines()]
    inp = input("CHAR: ").upper()
    while True:
        run()