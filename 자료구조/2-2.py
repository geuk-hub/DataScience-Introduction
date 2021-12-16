class Date :
    def __init__(self, year, month, day) :
        self.year = year
        self.month = month
        self.day = day
    def __gt__(self, rhs) :
    def __lt__(self, rhs) :
    def __str__(self) :

def findMinMax(lst) :

def main() :
    inFile = open("input.txt","r")
    lst = []
    while True :
        line = inFile.readline()
        if line == "" :
            break
        date = [int(i) for i in line.split()]
        lst.append(Date(date[0], date[1], date[2]))
    for i in range(len(lst)) :
        print(lst[i])
    min, max = findMinMax(lst)
    print()
    print("earlist date : ", min)
    print("latest data : ", max)
    inFile.close()


main()