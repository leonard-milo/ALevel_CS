from functools import reduce
import time

def flatten(list):
    return reduce(lambda x, y: x+y, list)

def get_num_digit(list):
    m = 0
    for item in list:
        m = max(m, item)
    return len(str(m))

def radix(list, num_digits):
    for digit in range(num_digits):
        buck = [[] for _ in range(10)]
        for item in list:
            num = (item // 10 ** digit) % 10
            buck[num].append(item)
        list = flatten(buck)
    return list

def findlist():
    list = []
    f = open("randomlist.txt", "r")
    if f.mode == 'r':
        fileContents = f.readlines()
        for line in fileContents:
            list.append(int(line))
            f.close()
    return list

def storelist(list):
    f = open("sortedlist_large.txt", "w+")
    for l in range(len(list)):
        num = list[l]
        f.write(f"{num}\n")
    f.close

def test():
    #mylist = [55,45,3,289,213,1,288,53,2]
    mylist = findlist()
    n = get_num_digit(mylist)
    st = time.time()
    mslist = radix(mylist, n)
    et = time.time()
    #print(mslist)
    print(et - st)
    storelist(mslist)

def main():
    test()

if __name__ == "__main__":
    main()