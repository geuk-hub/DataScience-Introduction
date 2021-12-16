import random
import copy

def sortGapInsertion(A, first, last, gap) :
    for i in range(first + gap, last + 1, gap) :
        key = A[i]
        j = i - gap
        while j >= first and key < A[j] :
            A[j + gap] = A[j]
            j = j - gap
        A[j + gap] = key

def shellSort(A) :
    n = len(A)
    gap = n//2
    while gap > 0 :
        if gap % 2 == 0 :
            gap += 1
        for i in range(gap) :
            sortGapInsertion(A, i, n - 1, gap)
        gap = gap // 2

def heapify(arr, n, i) :
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and arr[i] < arr[l] :
        largest = l
    if r < n and arr[largest] < arr[r] :
        largest = r
    if largest != i :
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr) :
    n = len(arr)
    for i in range(n//2, -1, -1) :
        heapify(arr, n, i)
    
    for i in range(n-1, 0, -1) :
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def mergeSort(A) :
    if len(A) > 1:
        mid = len(A) // 2
        left = A[:mid]
        right = A[mid:]
        mergeSort(left)
        mergeSort(right)
        merge(A, left, right)

def merge(A, left, right) :
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right) :
        if left[i] < right[j] :
            A[k] = left[i]
            k, i = k + 1, i + 1
        else :
            A[k] = right[j]
            k, j = k + 1, j + 1
    while i < len(left) :
        A[k] = left[i]
        k, i = k + 1, i + 1
    while j < len(right) :
        A[k] = right[j]
        k, j = k + 1, j + 1

def quickSort(A, left, right) :
    if left < right :
        q = partition(A, left, right)
        quickSort(A, left, q - 1)
        quickSort(A, q + 1, right)

def partition(A, left, right) :
    low = left + 1
    high = right
    pivot = A[left]
    while low <= high :
        while low <= right and A[low] < pivot :
            low += 1
        while high >= left and A[high] > pivot :
            high -= 1
        if low < high :
            A[low], A[high] = A[high], A[low]
            low, high = low + 1, high - 1
        else :
            break
    A[left], A[high] = A[high], A[left]
    return high

def main() :
    n = int(input("Enter a number of data : "))
    data = []
    for i in range(n) :
        numbers = random.randint(0, n)
        data.append(numbers)
    
    d = copy.deepcopy(data)
    print("Before shell sort :\t", d)
    shellSort(d)
    print("After shell sort :\t", d)
    d = copy.deepcopy(data)
    print("\nBefore heap sort :\t", d)
    heapSort(d)
    print("After heap sort :\t", d)
    d = copy.deepcopy(data)
    print("\nBefore merge sort :\t", d)
    mergeSort(d)
    print("After merge sort :\t", d)
    d = copy.deepcopy(data)
    print("\nBefore quicksort :\t", d)
    quickSort(d, 0, len(d) - 1)
    print("After quicksort : \t", d)

main()