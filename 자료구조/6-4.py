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
            self.count -= 1
            self.items = self.items[self.front-1 : ]
            
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
            return self.items[(self.front) % self.MAX_SIZE]
    def size(self) :
        return self.count
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
        self.dequeue()
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
            self.rear = self.rear - 1
            self.count -= 1
            if self.rear < 0 :
                self.rear = self.MAX_SIZE - 1
            self.items = self.items[self.front-1 : self.rear+1]
    def getRear(self) :
        return self.items[self.rear]

infile = open('input1.txt')
infile = infile.readlines()

for i in infile[:] :
    s = CircularDeque()
    q = CircularDeque()    
    for j in i[:-1] :
        q.enqueue(j)
    for j in i[:-1] :
        s.enqueue(j.lower())
    a = []
    for i in s.items[:] :
        if i == None :
            continue
        else :
            a.append(i.upper())

    s.items = a
    s.MAX_SIZE = len(a)+1
    s.rear = len(a)-1
    s.count = len(a)

    while(1) :
        if s.getFront() == s.getRear() :
            s.deleteFront()
            s.deleteRear()
            if s.size() == 1 or s.size() == 0 :
                for i in a[:]:
                    print(i, end= "")
                print("")
                print("==> palindrome")
                break
        elif s.getFront() != s.getRear() :
            for i in a[:]:
                print(i, end= "")
            print("")
            print("==> not palindrome")
            break
    