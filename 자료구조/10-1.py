class BSTNode :
    def __init__(self, item, left = None, right = None) :
        self.item = item
        self.left = left
        self.right = right

class BSTree :
    def __init__(self) :
        self.root = None
        self.insertSuccess = None
        self.deleteSuccess = None
        
    def insert(self, data) :
        self.root = self.insert1(self.root, data)
        return self.insertSuccess
    def insert1(self, node, data) :
        if node == None :
            node = BSTNode(data)
            self.insertSuccess = True
        elif data > node.item :
            node.right = self.insert1(node.right, data)
        elif data < node.item :
            node.left = self.insert1(node.left, data)
        return node

    def search(self, data) :
        return self.search1(self.root, data)
    def search1(self, node, data) :
        if node == None :
            return False
        elif data > node.item :
            return self.search1(node.right, data)
        elif data < node.item :
            return self.search1(node.left, data)
        else :
            return True

    def delete(self, data) :
        self.root = self.delete1(self.root, data)
        return self.deleteSuccess
    def delete1(self, node, data) :
        if node == None :
            self.deleteSuccess = False
        elif data > node.item :
            node.right = self.delete1(node.right, data)
        elif data < node.item :
            node.left = self.delete1(node.left, data)
        else :
            self.deleteSuccess = True
            if node.right == None :
                node = node.left
            elif node.left == None :
                node = node.right
            else :
                maxNode = node.left
                while maxNode.right != None :
                    maxNode = maxNode.right
                node.item = maxNode.item
                node.left = self.delete1(node.left, maxNode.item)
        return node


    def print(self) :
        self.print1(self.root, 0)
    def print1(self, node, skip) :
        if node != None :
            self.print1(node.right, skip + 10)
            for i in range(skip) :
                print(" ", end = "")
            print(node.item, end = "")
            if node.left != None :
                print(",L", end = "")
            if node.right != None :
                print(",R", end = "")
            print()
            self.print1(node.left, skip + 10)

        

def main() :
    t = BSTree()
    print("Enter a command : i(nsert), s(earch), d(elete), p(rint) or q(uit)")
    while True :
        print("> ", end = "")
        line = input().split()
        command = line[0]
        if command == 'i' :
            item = int(line[1])
            if t.insert(item) :
                print(item, "is inserted")
            else :
                print("Not inserted : same data")
        elif command == 's' :
            item = int(line[1])
            if t.search(item) :
                print(item, "is found")
            else :
                print("No such item in the tree")
        elif command == 'd' :
            item = int(line[1])
            if t.delete(item) :
                print(item, "is deleted")
            else :
                print("No such item in the tree")
        elif command == 'p' :
            t.print()
        elif command == 'q' :
            break
    
main()