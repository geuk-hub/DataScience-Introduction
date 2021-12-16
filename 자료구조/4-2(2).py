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

def change(number) :
    s = Stack()
    while(1) :
        if number // 2 == 1 :
            s.push(number % 2)
            s.push(number // 2)
            break
        s.push(number % 2)
        number //= 2
    return s.top[::-1]


def main() :
    while(1) :
        data = int(input("Enter a decimal number : "))
        if data == -1 :
            break
        number = change(data)
        decimal_number = ""
        for i in number :
            print(i)
            print(type(i))
            decimal_number += str(i)
        print("{} ==> {}".format(data, str(decimal_number)))


main()