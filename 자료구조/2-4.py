class Date:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day

    def lastDayOfTheMonth(self):
        if self.month == 2:
            if self.year % 4 == 0 and self.year % 100 != 0 or self.year%400 == 0:
                return 29
            else:
                return 28
        elif self.month == 4 or self.month ==6 or self.month ==9 or self.month ==11:
            return 30
        else:
            return 31

    def increment(self):
        if self.day == self.lastDayOfTheMonth():
            self.day = 1
            if self.month == 12:
                self.month = 1
                self.year += 1
            else:
                self.month += 1
        else:
            self.day += 1
        return self

    def __str__(self):
        return "%d/%d/%d"%(self.year,self.month,self.day)

    def __eq__(self, other):
        return self.year==other.year and self.month==other.month and self.day==other.day


def main():
    inFile=open("input3.txt",'r')
    lst=[]
    lst2=[]
    num=0
    while True:
        line=inFile.readline()
        if line=="":
            break

        date=[int(i) for i in line.split()]
        lst.append(Date(date[0],date[1],date[2]))
        lst2.append(Date(date[3],date[4],date[5]))
        print("%d/%d/%d\t"%(date[0],date[1],date[2]),end="")
        print("\t%d/%d/%d\t==>"%(date[3], date[4], date[5]),end="")

        lstlen=0
        lst2len=0

        day=0
        for i in range(0, 3):
            lstlen += date[i]

        for i in range(3, 6):
            lst2len += date[i]

        while lst[num]!=lst2[num]:
            if lstlen<lst2len:
                Date.increment(lst[num])
                day += 1
            else:
                Date.increment(lst2[num])
                day-=1
        print("%10d 일 경과"%day)



        num+=1


    inFile.close()

main()