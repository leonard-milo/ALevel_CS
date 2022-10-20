import random
import time

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

def storelist(list):
    f = open("bubble_sort_list.txt", "w+")
    for l in range(len(list)):
        num = list[l]
        f.write(f"{num}\n")
    f.close

def test():
    '''
    mylist = [5,2,1,3,6,4]
    mslist1 = bubblesort(mylist)
    print(mslist1)
    '''
    rndlist = rndlistgenerator(1024)
    mslist2 = bubblesort(rndlist)
    # print(mslist2)
    storelist(mslist2)

def timecal(N):
    rndlist = rndlistgenerator(1024 * N)
    st = time.time()
    bubblesort(rndlist)
    et = time.time()
    return et - st

def tcpxty():
    print(timecal(4) / timecal(1))
    print(timecal(5) / timecal(1))

def main():
    #test()
    tcpxty()
    

if __name__ == "__main__":
    main()