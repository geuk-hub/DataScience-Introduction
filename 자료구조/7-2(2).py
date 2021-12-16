class DNode :
    def __init__(self, item, prev = None, next = None) :
        self.item = item
        self.prev = prev
        self.next = next

class CircularDoublyLinkedList :
    def __init__(self) :
        self.head = None
    
    def isEmpty(self) :
        return self.head == None
    def clear(self) :
        self.head = None
    def addFront(self, item) :
        data = DNode(item)
        if self.isEmpty() :
            self.head = data
            self.head.next = data
            self.head.prev = data
        else :
            data.prev = self.head.prev
            data.next = self.head
            self.head.prev.next = data
            self.head.prev = data
            self.head = data

    def addRear(self, item) :
        node = DNode(item)
        if self.isEmpty() :
            self.head = node
            self.head.prev = node
            self.head.next = node
        else :
            node.prev = self.head.prev
            node.next = self.head
            self.head.prev.next = node
            self.head.prev = node
    
    def deleteFront(self) :
        if self.isEmpty() == False :
            data = self.head.item
            if self.size() == 1 :
                self.head = None
                return data
            self.head.next.prev = self.head.prev
            self.head.prev.next = self.head.next
            self.head = self.head.next
        return data

    def deleteRear(self) :
        if self.isEmpty() == False :
            data = self.head.item
            if self.size() == 1 :
                self.head = None
                return data
            self.head.prev.prev.next = self.head
            self.head.prev = self.head.prev.prev
        return data
    def peekFront(self) :
        return self.head.item
    def peekRear(self) :
        return self.head.prev.item
    def size(self) :
        count = 0
        if self.isEmpty() :
            return count
        else :
            data = self.head
            while(1) :
                count += 1
                data = data.next
                if data == self.head :
                    break
        return count
    def print(self) :
        if self.isEmpty() :
            print("")
        else :
            tmp = self.head
            while(1) :
                print(tmp.item, end = " ")
                tmp = tmp.next
                if tmp == self.head :
                    print("")
                    break
    def revPrint(self) :
        if self.isEmpty() == False :
            tmp = self.head.prev
            while(1) :
                print(tmp, end = " ")
                tmp = tmp.prev
                if tmp == self.head.prev :
                    print("")
                    break
        else :
            print("")
            

def main() :
    dq = CircularDoublyLinkedList()
    print("Enter a command : af(addFront), df(deleteFront), pf(peekFront), s(size)")
    print("ar(addRear), dr(deleteRear), pr(peekRear), rp(reversePrint) or q(uit)")

    while True :
        print("> ", end ="")
        line = input().split()
        command = line[0]
        if command == 'af' :
            item = line[1]
            dq.addFront(item)
        elif command == 'df' :
            print(dq.deleteFront())
        elif command == 'pf' :
            print(dq.peekFront())
        elif command == 'ar' :
            item = line[1]
            dq.addRear(item)
        elif command == 'dr' :
            print(dq.deleteRear())
        elif command == 'pr' :
            print(dq.peekRear())
        elif command == 'p' :
            dq.print()
        elif command == 'rp' :
            dq.revPrint()
        elif command == 's' :
            print("size :", dq.size())
        elif command == 'q' :
            break

main()