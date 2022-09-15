class Record:
    def __init__(self, key, name):
        self.key = key
        self.name = name

class HashTable:
    def __init__(self, size):
        self.tableSize = size
        self.collisions = 0
        self.list = []
        for i in range(self.tableSize):
            self.list.append(Record(None, ""))

    def insertRec(self, newRecord):
        index = self.hash(newRecord.key)
        if self.list[index].key != None:
            self.collisions += 1
        while self.list[index].key != None:
            index += 1
            if index >= self.tableSize:
                index = 0
        self.list[index] = newRecord

    def findRec(self, searchKey):
        index = self.hash(searchKey)

        while self.list[index].key != searchKey and self.list[index].key != None:
            index += 1
            if index > self.tableSize:
                index = 0

        if self.list[index].key != None:
            return self.list[index].key
        else:
            return None

    def hash(self, key):
        return key % self.tableSize

    def getCollisions(self):
        return self.collisions

    def display(self):
        counter = 0
        for record in self.list:
            print(counter, " ", record.key)
            counter += 1

def test(hashtable, customerIDs):
    for ID in customerIDs:
        newRecord = Record(ID, "")
        hashtable.insertRec(newRecord)
    hashtable.display()
    print("Collisions: ", hashtable.collisions)
    print(hashtable.findRec(95312))
    print(hashtable.findRec(14875))

def main():
    hashtable = HashTable(10)
    customerIDs = [45876, 32390, 95312, 64636, 23467]
    test(hashtable, customerIDs)

if __name__ == "__main__":
    main()