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
        self.data = []
        self.data2 = []

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
    
    def nodeCount(self) :
        return self.nodeCount1(self.root)
    def nodeCount1(self, node) :
        if node == None :
            return 0
        else :
            return 1 + self.nodeCount1(node.left) + self.nodeCount1(node.right)
    
    def count_height(self) :
        return self.count_height1(self.root)
    def count_height1(self, node) :
        if node == None :
            return 0
        hLeft = self.count_height1(node.left)
        hRight = self.count_height1(node.right)
        if hLeft > hRight :
            return hLeft + 1
        else :
            return hRight + 1
        
    def full(self) :
        if self.nodeCount() == 2 ** self.count_height() - 1 :
            return True
        else :
            return False
    
    def inorder(self) :
        self.inorder1(self.root)
        print()

    def inorder1(self, node) :
        if node != None :
            self.inorder1(node.left)
            print(node.item, end = " ")
            self.inorder1(node.right)

    def min(self) :
        curr = self.root
        while curr.left != None :
            curr = curr.left
        return curr.item
    
    def max(self) :
        curr = self.root
        while curr.right != None :
            curr = curr.right
        return curr.item

    def path(self) :
        self.node_search()
        for i in self.data :
            self.path_search(i)
            for j in self.data2 :
                print(j, end = " ")
            print()
            self.data2 = []
        self.data = []

    def node_search(self) :
        self.node_search1(self.root)
    def node_search1(self, curr) :
        if curr != None :
            if curr.left == None and curr.right == None:
                self.data.append(curr.item)
            if curr.left != None:
                self.node_search1(curr.left)
            if curr.right != None:
                self.node_search1(curr.right)

    def path_search(self, data) :
        curr = self.root
        self.data2.append(curr.item)
        while curr != None :
            if data < curr.item :
                curr = curr.left
                self.data2.append(curr.item)

            elif data > curr.item :
                curr = curr.right
                self.data2.append(curr.item)
            else :
                return True
        return False


def main() :
    t = BSTree()
    print("Enter a command : i(nsert), s(earch), d(elete), inorder(traversal),")
    print("nc(node count), min, max, full, path, p(rint), or q(uit)")
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
        elif command == 'full' :
            print(t.full())
        elif command == 'nc' :
            print("node count =", t.nodeCount())
        elif command == 'inorder' :
            t.inorder()
        elif command == 'max' :
            print("Max :", t.max())
        elif command == 'min' :
            print("Min :", t.min())
        elif command == 'path' :
            t.path()
        elif command == 'q' :
            break
    
main()