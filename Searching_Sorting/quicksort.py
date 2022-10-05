def quicksort(list, left, right):
    if left < right:
        partition_pos = partition(list, left, right)
        quicksort(list, left, partition_pos-1)
        quicksort(list, partition_pos+1, right)
    return list

def partition(list, left, right):
    i = left
    j = right - 1
    pivot = list[right]

    while i < j:
        while i < right and list[i] < pivot:
            i+=1
        while j > left and list[j] >= pivot:
            j-=1
        if i < j:
            list[i], list[j] = list[j], list[i]

    if list[i] > pivot:
        list[i], list[right] = list[right], list[i]

    return i

def test():
    mylist = [22,11,88,66,55,77,33,44]
    mslist = quicksort(mylist, 0, len(mylist) - 1)
    print(mslist)

def main():
    test()

if __name__ == "__main__":
    main()