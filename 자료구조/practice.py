import copy

data = [24, 15, 29, 11, 47, 12]

d = copy.deepcopy(data)

def Bubble_sorting1(data) :
    n = len(data)
    for i in range(n-1, 0, -1) :
        for j in range(i, 0, -1) :
            if data[j] < data[j-1] :
                data[j], data[j-1] = data[j-1], data[j]
        print("Pass %d: %s" %(n-i, data))

Bubble_sorting1(d)

def Selection_sorting1(data) : 
    n = len(data)
    for i in range(n) :
        hi = data[i]
        for j in range(i, n) :
            if data[j] < data[i] :
                hi = data[j]
        data[j], data[i]
        print("Pass %d: %s" %(i, data))

d = copy.deepcopy(data)
Selection_sorting1(d)