class ArrayList :
    def __init__(self) :
        self.items = []

    def add(self, elem) :
        self.items.append(elem)
    def remove(self, elem) :
        if self.find(elem) == False :
            print("No such element")
        else :
            self.items.remove(elem)
            print(elem, "removed")
    def insert(self, pos, elem) :
        self.items.insert(int(pos), elem)
    def delete(self, pos) :
        self.items.pop(pos-1)
    def isEmpty(self) :
        return self.size() == 0

    def getEntry(self, pos) :
        return self.items[int(pos)]
    def size(self) :
        return len(self.items)
    def clear(self) :
        self.items = []
    def find(self, item) :
        if item in self.items :
            return True
        return False
    def replace(self, pos, elem) :
        self.items[int(pos)] = elem
    def sort(self) :
        self.items.sort()
    def merge(self, lst) :
        for i in lst :
            self.items.append(i)
    def print(self, msg = "ArrayList") :
        print("ArrayList", len(self.items), self.items)
    def dup(self) :
        new = []
        for i in self.items :
            if i not in new :
                new.append()
        self.items = new

def main() :
    print("Enter a commad : i(nsert), d(elete), e(mpty), g(enEntry), c(lear), a(dd)")
    print("dup, remove, search, f(ind), r(eplace), s(ort), m(erge), p(rint): ")
    s = ArrayList()
    while(1) :
        data = list(input("> ").split())
        if data[0] == 'a' :
            s.add(data[1])
        elif data[0] == 'p' :
            s.print()
        elif data[0] == 'i' :
            s.insert(data[1], data[2])
        elif data[0] == 'e' :
            print(s.isEmpty())
        elif data[0] == 'g' :
            print(s.getEntry(data[1]))
        elif data[0] == 'remove' :
            s.remove(data[1])
        elif data[0] == 'search' :
            if s.find(data[1]) == True :
                print(data[1], "found")
            else :
                print("No such element")
        elif data[0] == 's' :
            s.sort()
        elif data[0] == 'r' :
            s.replace(data[1], data[2])
        elif data[0] == 'dup' :
            s.dup()
        elif data[0] == 'm' :
            new = []
            for i in data[1:] :
                new.append(i)
            s.merge(new)
        elif data[0] == 'q' :
            break

main()