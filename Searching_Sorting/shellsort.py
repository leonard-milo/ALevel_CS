def shellsort(list):
    size = len(list)
    interval = size // 2

    while interval > 0:
        for i in range(interval, size):
            anchor = list[i]
            j = i
            while j >= interval and list[j-interval] > anchor:
                list[j] = list[j-interval]
                j -= interval
            list[j] = anchor
        interval //= 2
    return list

def test():
    mylist = [21,38,29,17,4,25,11,32,9]
    mslist = shellsort(mylist)
    print(mslist)

def main():
    test()

if __name__ == "__main__":
    main()