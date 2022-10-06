import random

def linear(list, ele):
    ncompare = 0
    for i in range(len(list)):
        ncompare+=1
        if list[i] == ele:
            return True, ncompare
    return False, ncompare

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
    
    #element = random.randrange(1, len(mylist)+1)
    element = 1000
    exist, ncompare = linear(mylist, element)
    if exist:
        print(f"{element} exist")
    else:
        print(f"{element} do not exist")
    print(f"{ncompare} compares made")
    

def main():
    test()

if __name__ == "__main__":
    main()
