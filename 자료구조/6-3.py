class CircularQueue :
    def __init__(self) :
        self.MAX_SIZE = 3
        self.items = [None] * self.MAX_SIZE
        self.front = 0
        self.rear = 0
        self.count = 0
    def isEmpty(self) :
        return self.count == 0
    def isFull(self) :
        return self.front == (self.rear+1) % self.MAX_SIZE
    def clear(self) :
        self.front = 0
        self.rear = 0
        self.count = 0
    def enqueue(self, item) :
        if self.isFull() :
            self.resize()
        if not self.isFull() :
            self.rear = (self.rear+1) % self.MAX_SIZE
            self.items[self.rear] = item
            self.count += 1
    def dequeue(self) :
        if not self.isEmpty() :
            self.front = (self.front+1) % self.MAX_SIZE
            print(self.items[self.front])
            self.count -= 1
    def resize(self) :
        newitems = [None] * 2 * self.MAX_SIZE
        scan = (self.front+1) % self.MAX_SIZE
        for i in range(self.count):
            newitems[i+1] = self.items[scan]
            scan = (scan+1) % self.MAX_SIZE
        self.items = newitems
        self.front = 0
        self.rear = self.count
        self.MAX_SIZE = self.MAX_SIZE * 2
    def peek(self) :
        if not self.isEmpty() :
            print(self.items[(self.front+1) % self.MAX_SIZE])
    def size(self) :
        print("size: %d"%(self.count))
    def print(self) :
        out = []
        if self.front < self.rear :
            out = self.items[self.front+1:self.rear+1]
        elif self.front == self.rear :
            out = []
        else :
            out = self.items[self.front+1:self.MAX_SIZE] + self.items[0:self.rear+1]
        print(out)

class CircularDeque(CircularQueue) :
    def __init__(self) :
        super().__init__()
    def addRear(self, item) :
        self.enqueue(item)
    def deleteFront(self) :
        return self.dequeue()
    def getFront(self) :
        return self.peek()
    def addFront(self, item) :
        if self.isFull() :
            self.resize()
        if not self.isFull() :
            self.items[self.front] = item
            self.front = self.front - 1
            self.count += 1
            if self.front < 0 :
                self.front = self.MAX_SIZE - 1
    def deleteRear(self) :
        if not self.isEmpty() :
            item = self.items[self.rear]
            self.rear = self.rear - 1
            self.count -= 1
            if self.rear < 0 :
                self.rear = self.MAX_SIZE - 1
            print(item)
    def getRear(self) :
        print(self.items[self.rear])

print("Enter a command: af(addFront), df(deleteFront), gf(getFront), s(ize)")
print("ar(addRear), dr(deleteRear), gr(getRear), p(rint) or q(uit)")
s = CircularDeque()
while(1) :
    data = list(input("> ").split())
    if data[0] == "ar" :
        s.addRear(data[1])
    if data[0] == "af" :
        s.addFront(data[1])
    if data[0] == "p" :
        s.print()
    if data[0] == "s" :
        s.size()
    if data[0] == "gf" :
        s.getFront()
    if data[0] == "gr" :
        s.getRear()
    if data[0] == "dr" :
        s.deleteRear()
    if data[0] == "df" :
        s.deleteFront()
    if data[0] == "q" :
        break