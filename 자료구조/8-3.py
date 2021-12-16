import random, copy, time

def sequential_search(A, key, low, high) :
    for i in range(low, high) :
        if A[i] == key :
            return i
    return None

def binary_search(A, key, low, high) :
    if low <= high :
        middle = (low + high) // 2
        if key == A[middle] :
            return middle
        elif key < A[middle] :
            return binary_search(A, key, low, middle - 1)
        else :
            return binary_search(A, key, middle + 1, high)
    return None

n = int(input("Enter a number of data : "))
data = []
for i in range(n) :
    numbers = random.randint(0,n)
    data.append(numbers)
d = copy.deepcopy(data)
startTime = time.time()
d.sort()
endTime = time.time()
print("Python sort elapsed time : %.3f seconds\n" %(endTime - startTime))

while(1) :
    search_number = int(input("Enter a number to search : "))
    if search_number == -1 :
        break
    if sequential_search(data,search_number,0,len(d)) == None :
        print("%d is not in the list." %search_number)
        startTime = time.time()
        sequential_search(data,search_number,0,len(d))
        endTime = time.time()
        print("Sequential search elapsed time : %.3f seconds" %(endTime - startTime))
    else :
        print("%d is in the list at index %d"%(search_number, sequential_search(data,search_number,0,len(d))))
        startTime = time.time()
        sequential_search(data,search_number,0,len(d))
        endTime = time.time()
        print("Sequential search elapsed time : %.3f seconds" %(endTime - startTime))
    
    if binary_search(d, search_number, 0, len(d)-1) == None :
        print("%d is not in the list"%search_number)
        startTime = time.time()
        binary_search(d,search_number,0,len(d)-1)
        endTime = time.time()
        print("Binary search elapsed time : %.3f seconds\n" %(endTime - startTime))
    else :
        print("%d is in the list at index %d"%(search_number, binary_search(d,search_number,0,len(d)-1)))
        startTime = time.time()
        binary_search(d,search_number,0,len(d)-1)
        endTime = time.time()
        print("Binary search elapsed time : %.3f seconds\n" %(endTime - startTime))