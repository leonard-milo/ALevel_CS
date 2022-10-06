import random
from random import shuffle
import time

def rndlistgenerator(size):
    rndlist = []
    i = 0
    while i < size:
        num = random.randrange(1, size+1)
        if num not in rndlist:
            rndlist.append(num)
            i+=1
    return rndlist

def rndshuffle(size):
    list = [i for i in range(size)]
    shuffle(list)
    return list

def storelist(list):
    f = open("randomlist.txt", "w+")
    for l in range(len(list)):
        num = list[l]
        f.write(f"{num}\n")
    f.close

def test():
    N = 1024
    st = time.time()
    #rndlist = rndlistgenerator(1024 * N)
    rndlist = rndshuffle(1024 * N)
    et = time.time()
    print(et-st)
    #print(rndlist)
    storelist(rndlist)

def main():
    test()

if __name__ == "__main__":
    main()