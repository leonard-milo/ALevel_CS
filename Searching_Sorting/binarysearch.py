import random

def binarys(list, ele):
    last = len(list)-1
    i = 0
    count = 0
    while i < last:
        mid = (i + last) // 2
        count += 1
        if list[mid] == ele:
            return True, count
        elif list[mid] < ele:
            i = mid + 1
        else:
            last = mid -1
    return False, count

def findlist():
    list = []
    f = open("sortedlist.txt", "r")
    if f.mode == 'r':
        fileContents = f.readlines()
        for line in fileContents:
            list.append(int(line))
            f.close()
    return list

def test():
    mylist = findlist()
    #print(mylist)
    
    element = random.randrange(1, len(mylist)+1)
    #element = 1000
    exist, ncompare = binarys(mylist, element)
    if exist:
        print(f"{element} exist")
    else:
        print(f"{element} do not exist")
    print(f"{ncompare} compares made")
    

def main():
    test()

if __name__ == "__main__":
    main()