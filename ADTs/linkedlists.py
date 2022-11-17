class Node:
    def __init__(self, data, ptr):
        self.Data = data
        self.Ptr = ptr

class LinkedList:
    NullPtr = -1
    def __init__(self, size):
        self.dataListPtr = self.NullPtr
        self.freeListPtr = 0
        self.size = size
        self.store = [Node('?',i+1) for i in range(self.size)]
        self.store[self.size - 1].Ptr = self.NullPtr

    def resetStore(self):
        self.dataListPtr = self.NullPtr
        self.freeListPtr = 0
        self.store = [Node('?',i+1) for i in range(self.size)]
        self.store[self.size - 1].Ptr = self.NullPtr

    def insertItem(self, newItem):  # there is space in the array
        #  take node from free list and store data item
        if self.freeListPtr != self.NullPtr:
            newNodePtr = self.freeListPtr
            self.store[newNodePtr].Data = newItem
            self.freeListPtr = self.store[self.freeListPtr].Ptr
        
        #  find insertion point
        preNodePtr = self.NullPtr
        thisNodePtr = self.dataListPtr  #  start at beginning of list
        while thisNodePtr != self.NullPtr and self.store[thisNodePtr].Data < newItem:
            preNodePtr = thisNodePtr  #  remember this node
            thisNodePtr = self.store[thisNodePtr].Ptr

        #  insert new node at start of list
        if self.dataListPtr == self.NullPtr or preNodePtr == self.NullPtr:
            self.store[newNodePtr].Ptr = self.dataListPtr
            self.dataListPtr = newNodePtr
        else:  #  insert new node between previous node and this node
            self.store[newNodePtr].Ptr = self.store[preNodePtr].Ptr
            self.store[preNodePtr].Ptr = newNodePtr

    def findItem(self, item):
        currentNodePtr = self.dataListPtr  #  start at beginning of list
        while currentNodePtr != self.NullPtr and self.store[currentNodePtr].Data != item:
            currentNodePtr = self.store[currentNodePtr].Ptr
        return currentNodePtr  #  returns NullPtr if item not found

    def deleteItem(self, item):
        thisNodePtr = self.dataListPtr
        while thisNodePtr != self.NullPtr and self.store[thisNodePtr].Data != item:
            preNodePtr = thisNodePtr  #  remember this node
            thisNodePtr = self.store[thisNodePtr].Ptr

        if thisNodePtr != self.NullPtr:  #  node exists in list
            if thisNodePtr == self.dataListPtr:  #  first node to be deleted
                self.dataListPtr = self.store[self.dataListPtr].Ptr
            else:
                self.store[preNodePtr].Ptr = self.store[thisNodePtr].Ptr
            self.store[thisNodePtr].Ptr = self.freeListPtr
            self.freeListPtr = thisNodePtr

    def showDataList(self):
        print("Data List: ", self.getListData("data"))

    def showFreeList(self):
        print("Free List: ", self.getListData("free"))

    def showAllNodes(self, listID):
        if listID == "data":
            self.showDataList()
        else:
            self.showFreeList()

    def displayStore(self):
        print("index \t data \t pointer")
        for i in range(self.size):
            print(f"[{i}] \t {self.store[i].Data} \t {self.store[i].Ptr}")

    def showPointers(self):
        print(f"data ptr: {self.dataListPtr}\tfree ptr:{self.freeListPtr}")

    def getPointers(self):
        return self.dataListPtr, self.freeListPtr

    def getStore(self):
        dataList = []
        ptrList = []
        for n in range(self.size):
            dataList.append(self.store[n].Data)
            ptrList.append(self.store[n].Ptr)
        return dataList, ptrList

    def getListData(self, listID):
        List = []
        if listID == "data":
            currentNodePtr = self.dataListPtr
        else:
            currentNodePtr = self.freeListPtr
        while currentNodePtr != self.NullPtr:
            List.append(self.store[currentNodePtr].Data)
            currentNodePtr = self.store[currentNodePtr].Ptr
        return List
            
    def getListPtrs(self, listID):
        List = []
        if listID == "data":
            currentNodePtr = self.dataListPtr
        else:
            currentNodePtr = self.freeListPtr
        while currentNodePtr != self.NullPtr:
            List.append(self.store[currentNodePtr].Ptr)
            currentNodePtr = self.store[currentNodePtr].Ptr
        return List

def test():
    mylist = LinkedList(10)
    mylist.insertItem('B')
    mylist.insertItem('D')
    mylist.insertItem('A')

    mylist.displayStore()
    mylist.showPointers()
    mylist.showAllNodes("data")
    mylist.showAllNodes("free")

    print(mylist.findItem('D'))

    mylist.deleteItem('A')
    mylist.displayStore()
    mylist.showPointers()
    mylist.showAllNodes("data")
    mylist.showAllNodes("free")

    mylist.deleteItem('D')
    mylist.displayStore()
    mylist.showPointers()

def main():
    test()

if __name__ == "__main__":
    main()