class Date:
    def __init__(self,year,month,day,increase):
        self.year=year
        self.month=month
        self.day=day
        self.increase=increase

    def lastDayOfTheMonth(self):
        if self.month == 2:
            if self.year % 4 == 0 and (self.year % 100 != 0 or self.year%400 == 0):
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



def main():
    inFile=open("input2.txt",'r')
    lst=[]
    num=0
    while True:
        line=inFile.readline()
        if line=="":
            break
        date=[int(i) for i in line.split()]
        lst.append(Date(date[0],date[1],date[2],date[3]))
        print("%d/%d/%d\t%7d일 후 ==>\t"%(date[0],date[1],date[2],date[3]),end="")
        for i in range(date[3]):
            Date.increment(lst[num])
        print(lst[num])
        num+=1
    inFile.close()

main()