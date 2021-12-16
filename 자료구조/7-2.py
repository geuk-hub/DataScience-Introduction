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
            self.head = node

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
            count = self.size()
            if count == 1 :
                self.head = None
            else :
                self.head.next.prev = self.head.prev
                self.head.prev.next = self.head.next
                self.head = self.head.next
            return data
    def deleteRear(self) :
        if self.isEmpty() == False :
            data = self.head.prev.item
            count = self.size()
            if count == 1 :
                self.head = None
            else :
                self.head.prev.prev.next = self.head
                self.head.prev = self.head.prev.prev
            return data
    def peekFront(self) :
        if self.isEmpty() == False :
            return self.head.item
    def peekRear(self) :
        if self.isEmpty() == False :
            return self.head.prev.item
    
    def size(self) :
        tmp = self.head
        count = 0
        if self.isEmpty() == False :
            while(1) :
                count += 1
                tmp = tmp.next
                if tmp == self.head :
                    break
        return count
    def print(self) :
        if self.isEmpty() == False :
            data = self.head
            while(1) :
                print(data.item, end = " ")
                data = data.next
                if data == self.head :
                    print("")
                    break
        else :
            print("")

    def revPrint(self) :
        if self.isEmpty() == False :
            data = self.head.prev
            while(1) :
                print(data.item, end = " ")
                data = data.prev
                if data == self.head.prev :
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
