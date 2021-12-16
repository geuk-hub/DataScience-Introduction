class Set:
    def __init__(self):
        self.items=[]
    def __eq__(self, setB) :
        return self.items == setB
    def insert(self,elem):
        if elem not in self.items:
            self.items.append(elem)
    def delete(self,elem):
        if elem in self.items:
            self.items.remove(elem)
    def union(self,setB): #합집합
        return list(set(self.items).union(set(setB.items)))
    def intersect(self,setB): #교집합
        return list(set(self.items).intersection(set(setB.items)))
    def difference(self,setB): #차집합
        return list(set(self.items).difference(set(setB.items)))
    def isSubset(self, setB): #부분집합
        return set(self.items).issubset(set(setB.items))
    def isProperSubset(self, setB) : #진부분집합
        return set(self.items) < set(setB.items)
    def size(self):
        return len(self.items)
    def print(self,msg):
        print(msg)

def test(setA, setB) :
    print("SetA: ", setA.items)
    print("SetB: ", setB.items)
    if setA == setB :
        print("A equal B: True")
    else :
        print("A equal B: False")
    print("A subset B: ", setA.isSubset(setB))
    print("A proper subset B: ", setA.isProperSubset(setB))
    print("A union B: ",setA.union(setB))
    print("A intersect B: ", setA.intersect(setB))
    print("A difference B: ", setA.difference(setB))
    print("")

def main() :
    setA = Set()
    setA.insert(2)
    setA.insert(3)
    setA.insert(4)
    
    setB = Set()
    setB.insert(2)
    setB.insert(3)
    setB.insert(4)

    setC = Set()
    setC.insert(2)
    setC.insert(3)
    setC.insert(4)
    setC.delete(4)

    test(setA, setB)
    test(setA, setC)
    test(setC, setA)

main()