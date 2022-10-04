import random

def bubblesort(list):
    swapcounter = -1
    size = len(list)
    while swapcounter != 0:
        swapcounter = 0
        for i in range(size-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                swapcounter+=1
            #print(list) # check
        size-=1
    return list

def rndlistgenerator(size):
    rndlist = []
    i = 0
    while i < size:
        num = random.randrange(1, size+1)
        if num not in rndlist:
            rndlist.append(num)
            i+=1
    return rndlist

def main():
    mylist = [5,2,1,3,6,4]
    mslist = bubblesort(mylist)
    #print(mslist)
    rndlist = rndlistgenerator(1024)
    #print(bubblesort(rndlist))


if __name__ == "__main__":
    main()