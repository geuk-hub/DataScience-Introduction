class Student :
    def __init__(self, number, name, score) :
        self.number = number
        self.name = name
        self.score = score
    def __str__(self) :
        return "[" + str(self.number) + ", " + self.name + ", " + str(self.score) + "]"

class Node :
    def __init__(self, item, next = None) :
        self.item = item
        self.next = next

class Entry :
    def __init__(self, key, value) :
        self.key = key
        self.value = value
    def __str__(self) :
        return str(self.key) + ":" + str(self.value)

class HashTable : 
    def __init__(self, size) :
        self.table = [None] * size
        self.tableSize = size
    
    def hash(self, key) :
        sum = 0
        for ch in str(key) :
            sum += ord(ch)
        return sum % self.tableSize

    def insert(self, key, value) :
        idx = self.hash(key)
        self.table[idx] = Node(Entry(key, value), self.table[idx])

    def search(self, key) :
        idx = self.hash(key)
        node = self.table[idx]
        while node != None : 
            if node.item.key == key :
                return node.item
            node = node.next
        return None 

    def delete(self, key) :
        idx = self.hash(key)
        node = self.table[idx]
        before = None
        while node != None :
            if node.item.key == key :
                if before == None :
                    self.table[idx] = node.next
                else :
                    before.next = node.next
                return True
            before = node
            node = node.next
                
    def print(self) :
        for idx in range(len(self.table)) :
            node = self.table[idx]
            if node != None :
                print("[%d]" %idx, end = "")
                while node != None :
                    print("\t", node.item)
                    node = node.next
            else :
                print("[%d]" %idx)

def main() :
    inFile = open("student.txt", "r")
    ht = HashTable(5)
    while True :
        line = inFile.readline()
        if line == '' :
            break
        lst = line.split()
        s = Student(int(lst[0]), lst[1], float(lst[2]))
        ht.insert(lst[0], s)
    ht.print()
    print("Enter a command : i(nsert), d(elete), s(earch), p(rint), or q(uit)")
    while True :
        command = input("> ")
        if command == 'i' :
            print("Enter student number, name, score : ", end ="")
            line = input().split()
            s = Student(int(line[0]), line[1], float(line[2]))
            ht.insert(line[0], s)
        elif command == 'd' :
            print("Enter student number : ", end = "")
            number = input()
            if ht.delete(number) != None :
                print(str(number) + " deleted")
            else :
                print(str(number) + " not found")
        elif command == 's' :
            print("Enter student number : ", end ="")
            number = input()
            s = ht.search(number)
            if s != None :
                print(s.value)
            else : 
                print(str(number) + " not found")
        elif command == "p" :
            ht.print()
        elif command == "q" :
            break

main()