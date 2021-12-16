import copy

data = [24, 15, 29, 11, 47, 12]

def Bubble_sorting(data) :
    A = data
    n = len(A)
    for i in range(n-1, 0, -1) :
        
        for j in range(i) :
            if A[j] > A[j+1] :
                A[j], A[j+1] = A[j+1], A[j]
        print("Pass %d: %d"%(n-i, A) )

Bubble_sorting(data)