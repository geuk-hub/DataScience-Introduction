class BTNode:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

class BTree:
    def __init__(self):
        self.root = None
    def buildTree(self):
        g = BTNode(12)
        d = BTNode(15, g)
        b = BTNode(10, None, d)
        e = BTNode(25)
        f = BTNode(55)
        c = BTNode(30, e, f)
        self.root = BTNode(20, b, c)
    def inorder(self) :
        self.inorder1(self.root)
        print()
    def inorder1(self, node) :
        if node != None :
            self.inorder1(node.left)
            print(node.item, end = " ")
            self.inorder1(node.right)
    def preorder(self) :
        self.preorder1(self.root)
        print()
    def preorder1(self, node) :
        if node != None :
            print(node.item, end = " ")
            self.preorder1(node.left)
            self.preorder1(node.right)

    def postorder(self) :
        self.postorder1(self.root)
        print()
    def postorder1(self, node) :
        if node != None :
            self.postorder1(node.left)
            self.postorder1(node.right)
            print(node.item, end = " ") 
    def nodeCount(self) :
        return self.nodeCount1(self.root)
    def nodeCount1(self, node) :
        if node == None :
            return 0
        else :
            return 1 + self.nodeCount1(node.left) + self.nodeCount1(node.right)

    def leafCount(self) :
        return self.leafCount1(self.root)

    def leafCount1(self, node) :
        if node != None :
            lLeft = self.leafCount1(node.left)
            lRight = self.leafCount1(node.right)    
            if node.left == None and node.right == None :
                return 1
            if lLeft == None :
                lLeft = 0
            if lRight == None :
                lRight = 0
            return lLeft + lRight
    
    def height(self) :
        return self.height1(self.root)
    def height1(self, node) :
        if node == None :
            return 0
        hLeft = self.height1(node.left)
        hRight = self.height1(node.right)
        if hLeft > hRight :
            return hLeft + 1
        else :
            return hRight + 1
    def print(self) :
        node = self.root
        self.print1(node, 0)

    def print1(self, node, number) :
        if node != None :
            
            self.print1(node.right, number + 1)
            for i in range(0, number) :
                print("\t", end = "")
            
            #if self.root == node :
            #    pass
            #elif self.root.left == node or self.root.right == node :
            #    print("\t", end = "")
            #elif self.root.right.right == node or self.root.left.right == node or self.root.right.left == node :
            #    print("\t\t", end = "")
            #else :
            #    print("\t\t\t", end = "")
            
            print(node.item, end = "")
            if node.left != None :
                print(",L", end = "")
            if node.right != None :
                print(",R", end = "")
            print()
            
            #if node.right != None and node.left != None :
            #    print("%d,L,R" %node.item)
            #elif node.right != None and node.left == None :
            #    print("%d,R" %node.item)
            #elif node.right == None and node.left != None :
            #    print("%d,L" %node.item)
            #else :
            #    print(node.item)

            self.print1(node.left, number + 1)

def main() :
    bt = BTree()
    print("Enter a command : bt(build tree), inorder(traversal), pre(order traversal),")
    print("post(order traversal), nc(node count), lc(leaf count), h(eight),")
    print("pp(pretty print), or q(uit)")
    while True :
        print("> ", end = "")
        line = input().split()
        command = line[0]
        if command == 'bt' :
            bt.buildTree()
        elif command == 'inorder' :
            bt.inorder()
        elif command == 'pre' :
            bt.preorder()
        elif command == 'post' :
            bt.postorder()
        elif command == 'nc' :
            print("node count = ", bt.nodeCount())
        elif command == 'lc' :
            print("leaf count = ", bt.leafCount())
        elif command == 'h' :
            print("height = ", bt.height())
        elif command == 'pp' :
            bt.print()
        elif command == 'q' :
            break

main()