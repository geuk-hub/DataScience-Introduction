import random, copy, time

def bubble_sort(A) :
    n = len(A)
    for i in range(n-1, 0, -1) :
        for j in range(i,0,-1) :
            if A[j] < A[j-1] :
                A[j], A[j-1] = A[j-1], A[j]

def selection_sort(A) :
    n = len(A)
    for i in range(n-1) :
        least = i
        for j in range(i+1, n) :
            if A[j]< A[least] :
                least = j
        A[i], A[least] = A[least], A[i]

def insertion_sort(A) :
    n = len(A)
    for i in range(1,n) :
        key = A[i]
        j = i-1
        while j >=0 and A[j] > key :
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key

while(1) :
    n = int(input("Enter a number of data : "))
    if n == -1 :
        break
    data = []
    for i in range(n) :
        numbers = random.randint(0,n)
        data.append(numbers)
    d = copy.deepcopy(data)
    startTime = time.time()
    bubble_sort(d)
    endTime = time.time()
    print("Bubble sort elapsed time : %.3f seconds" %(endTime - startTime))
    startTime = time.time()
    selection_sort(d)
    endTime = time.time()
    print("Selection sort elapsed time : %.3f seconds" %(endTime - startTime))
    startTime = time.time()
    insertion_sort(d)
    endTime = time.time()
    print("Insertion sort elapsed time : %.3f seconds" %(endTime - startTime))
    startTime = time.time()
    d.sort()
    endTime = time.time()
    print("Python sort elapsed time : %.3f seconds\n" %(endTime - startTime))