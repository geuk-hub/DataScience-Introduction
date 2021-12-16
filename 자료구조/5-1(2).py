MAX_SIZE = 3
class CircularQueue :
    def __init__(self) :
        self.items = [None] * MAX_SIZE
        self.front = 0
        self.rear = 0
        self.count = 0
        self.maxSize = MAX_SIZE
    
    def isEmpty(self) :
        return self.count == 0
    def isFull(self) :
        return self.front == (self.rear + 1) % self.maxSize
    def clear(self) :
        self.front = 0
        self.rear = 0
        self.count = 0
    def enqueue(self,item) :
        if self.isFull() :
            self.resize()
        self.rear = (self.rear + 1) % self.maxSize
        self.items[self.rear] = item
        self.count += 1
    def dequeue(self) :
        if self.isEmpty() == False :
            self.front = (self.front + 1) % self.maxSize
            self.count -= 1
        return self.items[self.front] 
    def resize(self):
        newItems = [None] * 2 * self.maxSize
        scan = (self.front + 1) % self.maxSize
        for i in range(self.count):
            newItems[i + 1] = self.items[scan]
            scan = (scan + 1) % self.maxSize
        self.items = newItems
        self.front = 0
        self.rear = self.count
        self.maxSize = 2*self.maxSize 
    def peek(self) :
        if self.isEmpty() == False :
            return self.items[(self.front + 1) % self.maxSize]
    def size(self) :
        return self.count
    def print(self) :
        out = []
        if self.front < self.rear :
            out = self.items[self.front + 1 : self.rear + 1]
        else :
            out = self.items[self.front+1 : self.maxSize] + self.items[0:self.rear+1]
        print(out)
    
def main() :
    print("Enter a commad :")
    s = CircularQueue()
    while(1) :
        data = list(input("> ").split())
        if data[0] == 'e' :
            s.enqueue(data[1])
        elif data[0] == 'p' :
            s.print()
        elif data[0] == 'd' :
            print(s.dequeue())
        elif data[0] == 's' :
            print(s.size())
        elif data[0] == 'peek' :
            print(s.peek())
        elif data[0] == 'q' :
            break

main()