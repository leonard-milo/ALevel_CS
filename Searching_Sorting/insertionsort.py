def insertionsort(list):
    size = len(list)
    for i in range(1, size):
        current = list[i]
        place = i - 1
        if list[place] > current:
            while place >= 0 and list[place] > current:
                list[place+1] = list[place]
                place-=1
            list[place+1] = current
        print(list)
    return list

def test():
    mylist = [8,2,4,1,3]
    slist = insertionsort(mylist)
    print(slist)

def main():
    test()
    pass

if __name__ == "__main__":
    main()