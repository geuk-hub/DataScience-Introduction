class PriorityQueue :
    def __init__(self) :
        self.items = []
        self.count = 0
    def size(self) :
        return self.count
    def isEmpty(self) :
        return self.count == 0
    def enqueue(self, item) :
        self.items.append(item)
        self.count += 1
        self.moveUp(0, self.count - 1)
    def moveUp(self, first, last) :
        while last > first :
            parent = (last - 1) // 2
            if self.items[parent] < self.items[last] :
                self.items[parent], self.items[last] = self.items[last], self.items[parent]
                last = parent
            else :
                break
    def dequeue(self) :
        if not self.isEmpty() :
            item = self.items[0]
            self.count -= 1
            self.items[0] = self.items[self.count]
            self.moveDown(0, self.count - 1)
            self.items.pop(-1)
            return item
    def moveDown(self, first, last) :
        leftChild = 2*first + 1
        while leftChild <= last :
            if leftChild == last :
                maxChild = leftChild
            else :
                rightChild = 2*first + 2
                if self.items[leftChild] <= self.items[rightChild] :
                    maxChild = rightChild
                else :
                    maxChild = leftChild
            if self.items[first] < self.items[maxChild] :
                self.items[first], self.items[maxChild] = self.items[maxChild], self.items[first]
                first = maxChild
                leftChild = 2*first + 1
            else :
                break

    def print(self) :
        for i in self.items :
            print(i, end = " ")
        print()

    def display(self) :
        data = 0
        number = 0
        self.display1(data, number)

    def display1(self, data, number) :
        if self.count > data :
            self.display1(2*data+2, number + 1)
            for i in range(0, number) :
                print("\t", end = "")
            print(self.items[data])
            self.display1(2*data+1, number + 1)

    def sort(self) :
        data = []
        for i in range(self.count) :
            new = self.dequeue()
            data.insert(0, new)
        return data
        
def main() :
    pq = PriorityQueue()
    print("Enter a command : e(nqueue), d(equeue), empty, s(size)")
    print("p(rint), pp(pretty print), sort, or q(uit)")
    while True :
        print("> ", end = "")
        line = input().split()
        command = line[0]
        if command == 'e' :
            item = int(line[1])
            pq.enqueue(item)
        elif command == 'd' :
            print(pq.dequeue())
        elif command == 'empty' :
            print(pq.isEmpty())
        elif command == 'p' :
            pq.print()
        elif command == 'pp' :
            pq.display()
        elif command == 's' :
            print("size :", pq.size())
        elif command == 'sort' :
            print(pq.sort())
        elif command == 'q' :
            break

main()