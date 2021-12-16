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
            out = self.item[self.front+1:self.MAX_SIZE] + self.items[0:self.rear+1]
        print(out)

infile = open("input.txt", "r")
infile = infile.readlines()
str_set = CircularQueue()
int_set = CircularQueue()
float_set = CircularQueue()

for i in infile[:] :
    for j in i.split() :
        try :
            int(j)
            int_set.enqueue(j)
        except :
            try :
                float(j)
                float_set.enqueue(j)
            except :
                str_set.enqueue(j)


print("String data: ", end = "")
str_set.print()
print("Integer data: ", end = "")
int_set.print()
print("Float data: ", end = "")
float_set.print()

sum1 = 0
for i in int_set.items[:] :
    try :
        sum1 += int(i)
    except : 
        pass
print("Sum of integer data: ", sum1)

sum2 = 0
for i in float_set.items[:] :
    try :
        sum2 += float(i)
    except :
        pass
print("Sum of float data: ", sum2)