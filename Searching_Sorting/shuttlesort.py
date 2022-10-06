def shuttlesort(list):
    for i in range(1, len(list)):
        for j in range(i, 0, -1):
            if list[j] < list[j-1]:
                list[j-1], list[j] = list[j], list[j-1]
            else:
                break
    return list

def test():
    mylist = [21,38,29,17,4,25,11,32,9]
    mylist = [5,4,7,8,9,3,2,1]
    mslist = shuttlesort(mylist)
    print(mslist)

def main():
    test()

if __name__ == "__main__":
    main()