class Queue:
    def __init__(self, size):
        self.head = 0
        self.tail = -1
        self.numElements = 0
        self.size = size
        self.emptyItem = None
        self.store = [self.emptyItem for i in range(self.size)]

    def resetStore(self):
        self.head = 0
        self.tail = -1
        self.numElements = 0
        self.store = [self.emptyItem for i in range(self.size)]

    def addItem(self, newItem):
        success = False
        if self.numElements < self.size:
            self.tail = (self.tail+1) % self.size
            self.store[self.tail] = newItem
            self.numElements+=1
            success = True
        else:
            print("Add failed: Queue is full")
        return success

    def removeItem(self):
        success = False
        value = None
        if self.numElements != 0:
            value = self.store[self.head]
            self.store[self.head] = self.emptyItem
            self.head = (self.head+1) % self.size
            self.numElements-=1
            success = True
        else:
            print("Remove failed: Queue is empty")
        return success, value

    def getStore(self):
        return self.store
    
    def getPointer(self):
        return self.head, self.tail

    def getQueueIndexes(self):
        indexes = []
        head = self.head
        tail = self.tail
        while head != tail+1:
            indexes.append(head)
            head = (head+1) % self.size
        return indexes

    def getQueueData(self):
        data = []
        head = self.head
        tail = self.tail
        while head != tail+1:
            data.append(self.store[head])
            head = (head+1) % self.size
        return data

def test():
    size = 10
    myQueue = Queue(size)
    myQueue.removeItem()
    for item in range(size):
        myQueue.addItem(item)
    myQueue.getStore()
    myQueue.addItem(10)
    myQueue.resetStore()
    for item in range(1, 7):
        myQueue.addItem(item)
    myQueue.removeItem()
    myQueue.removeItem()
    myQueue.getStore()
    print(myQueue.getQueueIndexes())
    print(myQueue.getQueueData())
    

def main():
    test()

if __name__ == "__main__":
    main()