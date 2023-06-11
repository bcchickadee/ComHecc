# Defining Abstract Datatypes
# Stack
class Stack:
    def __init__(self):
        self.__stack__ = []
    def push(self, item):
        self.__stack__.append(item)
    def pop(self):
        return self.__stack__.pop()
    def peek(self):
        if not self.isEmpty():
            return self.__stack__[-1]
    def isEmpty(self):
        return not(bool(len(self.__stack__)))
    def size(self):
        return len(self.__stack__)
    def __str__(self):
        t = str(self.__stack__)[1:-1]
        return 'S<'+t+'>S'


# Queue
class Queue:
    def __init__(self):
        self.__queue__ = []
    def enqueue(self, e):
        self.__queue__.append(e)
    def dequeue(self):
        if not self.isEmpty():
            return self.__queue__.pop(0)
    def isEmpty(self):
        return not(bool(len(self.__queue__)))
    def peek(self):
        if not self.isEmpty():
            return self.__queue__[0]
    def size(self):
        return len(self.__queue__)
    def __str__(self):
        t = str(self.__queue__)[1:-1]
        return 'Q<'+t+'>Q'


# Vectors and their computations
class Vector:
    def __init__(self, li):
        self.__vec__ = li
    def dim(self):
        return len(self.__vec__)
    def __add__(self, self2):
        if self.dim() == self2.dim():
            newvec = []
            for i in range(self.dim()):
                newvec.append(self.__vec__[i] + self2.__vec__[i])
            return Vector(newvec)
        else:
            raise Exception("Dimensions are not the same!")
    def __sub__(self, self2):
        if self.dim() == self2.dim():
            newvec = []
            for i in range(self.dim()):
                newvec.append(self.__vec__[i] - self2.__vec__[i])
            return Vector(newvec)
        else:
            raise Exception("Dimensions are not the same!")
    def __str__(self):
        t = str(self.__vec__)[1:-1]
        return 'Vector('+t+')'

# =======================================
# Searching Algorithms
# Linear Search
def linearSearch(li, query):
    i = 0
    while li[i] != query:
        i += 1
    return i

# Binary Search
def binarySearch(li, query, low = 0, high = -1):
    if high == -1:
        high = len(li)
    li.sort()
    mid = (low + high) // 2
    if li[mid] == query:
        return mid
    elif li[mid] > query:
        high = mid - 1
        return binarySearch(li, query, low, high)
    elif li[mid] < query:
        low = mid + 1
        return binarySearch(li, query, low, high)

# =======================================
# Sorting Algorithms
# Bubble Sort
def bubbleSort(li):
    l = len(li)
    for i in range(l):
        for j in range(l-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li

# Selection Sort
def selectionSort(li):
    l = len(li)
    for i in range(l-1, -1, -1):
        ind = li.index(max(li[:i+1]))
        li[ind], li[i] = li[i], li[ind]
    return li
    
# Insertion Sort
def insertionSort(li):
    l = len(li)
    for i in range(1, l):
        ind = 0
        while li[i] > li[ind]:
            ind += 1
        a = li.pop(i)
        li.insert(ind, a)
    return li


# =======================================
# Divide and Conquer
# Tower of Hanoi
def towerHanoi(n, main = 'A', aux = 'B', dest = 'C'):
    if n == 1:
        print(f'Move plate from {main} to {dest}')
    else:
        towerHanoi(n-1, main, dest, aux)
        print(f'Move plate from {main} to {dest}')
        towerHanoi(n-1, aux, main, dest)

# Merge Sort
def mergeSort(li):
    def mergeOp(li1, li2):
        newlist = []
        while len(li1) != 0 and len(li2) != 0:
            if li1[0] <= li2[0]:
                newlist.append(li1.pop(0))
            else:
                newlist.append(li2.pop(0))
        if len(li1) == 0:
            while li2:
                newlist.append(li2.pop(0))
        elif len(li2) == 0:
            while li1:
                newlist.append(li1.pop(0))
        return newlist

    l = len(li)
    if l == 1:
        return li
    else:
        mid = l // 2
        return mergeOp(mergeSort(li[:mid]), mergeSort(li[mid:]))
        
