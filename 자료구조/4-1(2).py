class Stack :
    def __init__(self) :
        self.top = []
    def isEmpty(self) :
        return self.size() == 0
    def size(self) :
        return len(self.top)
    def clear(self) :
        self.top = []
    def push(self, item) :
        self.top.append(item)
    def pop(self) :
        return self.top.pop()
    def peek(self) :
        return self.top[-1]
    def __str__(self) :
        return str(self.top[::-1])

def main() :
    print("Enter a command : pop, push, peek, size, empty, p(rint), m(atch), q(uuit)")
    s = Stack()
    while(1) :
        data = list(input("> ").split())
        if data[0] == 'push' :
            s.push(data[1])
        elif data[0] == 'p' :
            print(s)
        elif data[0] == 'peek' :
            print(s.peek())
        elif data[0] == 'pop' :
            print(s.pop())
        elif data[0] == 'size' :
            print(s.size())
        elif data[0] == 'empty' :
            print(s.isEmpty())
        elif data[0] == 'q' :
            break

main()