def selecsort(list):
    size = len(list)
    for i in range(size-1):
        for j in range(i+1, size):
            if list[j] < list[i]:
                min_index = j
        if i != min_index:
            list[i], list[min_index] = list[min_index], list[i]
    return list

def test():
    mylist = [21,38,29,17,4,25,11,32,9]
    mslist = selecsort(mylist)
    print(mslist)

def main():
    test()

if __name__ == "__main__":
    main()