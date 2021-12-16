class Stack : 
    def __init__(self) :
        self.top = []
    def isEmpty(self) :
        return len(self.top) == 0
    def size(self) :
        return len(self.top)
    def clear(self) :
        self.top = []
    def push(self, item):
        self.top.append(item)
    def pop(self) :
        if not self.isEmpty() :
            return self.top.pop(-1)
    def peek(self) :
        if not self.isEmpty() :
            return self.top[-1]
    def __str__(self) :
        return str(self.top[::-1])

def check(number) :
    s = Stack()
    number2 = number
    while(1) :
        if number // 2 == 1 :
            s.push(number%2)
            s.push(number//2)
            break
        s.push(number%2)
        number = number // 2
    print("{0} ==> ".format(number2), end = "")
    for i in range(0, len(s.top)) :
        print(s.pop(), end="")
    print("")

def main() :
    while(1) :
        a = int(input("Enter a decimal number: "))
        if a == -1 :
            break
        check(a)
main()