def mergesort(list):
    if len(list) > 1:
        left_list = list[:len(list)//2]
        right_list = list[len(list)//2:]

        # recursion
        mergesort(left_list)
        mergesort(right_list)

        # merge
        l = 0       #left_list index
        r = 0       #right_list index
        m = 0       #merged list index
        while l < len(left_list) and r < len(right_list):
            if left_list[l] < right_list[r]:
                list[m] = left_list[l]
                l+=1
            else:
                list[m] = right_list[r]
                r+=1
            m+=1
        
        while l < len(left_list):
            list[m] = left_list[l]
            l+=1
            m+=1

        while r < len(right_list):
            list[m] = right_list[r]
            r+=1
            m+=1
        return list

def test():
    mylist = [5,2,1,3,6,4]
    #print(mylist)
    mergesort(mylist)
    print(mylist)


def main():
    test()

if __name__ == "__main__":
    main()