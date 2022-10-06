import random

def rndlistgenerator(size):
    rndlist = []
    i = 0
    while i < size:
        num = random.randrange(1, size+1)
        if num not in rndlist:
            rndlist.append(num)
            i+=1
    return rndlist

def storelist(list):
    f = open("randomlist.txt", "w+")
    for l in range(len(list)):
        num = list[l]
        f.write(f"{num}\n")
    f.close

def test():
    N = 8
    rndlist = rndlistgenerator(1024 * N)
    storelist(rndlist)

def main():
    test()

if __name__ == "__main__":
    main()