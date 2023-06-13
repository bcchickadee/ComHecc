# C_prac12.ipynb
# Chapter 12 Exercises

# Problem: Calculate Median
def bSort(li):
    '''
    Sort a list w/ Bubble Sort
    '''
    l = len(li)
    for i in range(l, -1, -1):
        for j in range(i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li

def calMed(li):
    '''
    Calculate the median of a sorted list
    '''
    if len(li) == 1:
        return li[0]
    elif len(li) == 2:
        return (li[0] + li[1]) / 2
    else:
        return calMed(li[1:-1])

l = list(map(int, input().split()))
print(int(calMed(bSort(l))))


# Problem: Cutline Calculator
def bSort(li):
    '''
    Sort a list w/ Bubble Sort
    '''
    l = len(li)
    for i in range(l, -1, -1):
        for j in range(i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li

def cutline(li, cut):
    '''
    Return cutline score of given list
    '''
    return li[-cut]

n = list(map(int, input().split()))[1]
l = list(map(int, input().split()))
print(cutline(bSort(l), n))


# Problem: Shaking Hands
num = list(map(int, input().split()))
m, n = num[0], num[1]

def ShakeHands(m, n):
    '''
    Calculate Number of Shaking Hands, which follow a specific condition
    '''
    shakeList = [i for i in range(m, n+1)]
    numShakes = 0
    for i in range(len(shakeList)):
        for j in range(i+1, len(shakeList)):
            c = shakeList[i] + shakeList[j]
            if c % 5 == 0 or c % 7 == 0:
                numShakes += 1
    return numShakes

print(ShakeHands(m, n))


# Problem: Sorting Documents w/ Bubble Sort
doclist = []
n = int(input())
for _ in range(n):
    doclist.append(input())

def organizer(txt):
    '''
    Organizes the text into the original document title
    '''
    txtlist = list(txt)
    txtlist = list(filter(lambda x: x.isalpha(), txtlist))
    
    return ''.join(txtlist[:int(len(txtlist)/2)])

def bSort(li):
    '''
    Sort a list w/ Bubble Sort
    '''
    l = len(li)
    for i in range(l, -1, -1):
        for j in range(i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li

orglist = [organizer(txt) for txt in doclist]
new_orglist = bSort(orglist.copy())
indlist = list(map(lambda x: orglist.index(x), new_orglist))
print(orglist, new_orglist, indlist)
for i in indlist:
    print(doclist[i])


# Problem: Raffle Event w/ Insertion Sort
from ast import literal_eval

def raffle(dic, n):
    '''
    Returns who is the last winner of the raffle.
    Prints the process of sorting.
    '''
    key = list(dic.keys())
    def iSort(li):
        l = len(li)
        for i in range(l):
            min_index = li.index(min(li[i:]))
            li[i], li[min_index] = li[min_index], li[i]
            print(li)
        return li
    key_sorted = iSort(key)
    return dic[key_sorted[n-1]]

print(raffle(literal_eval(input()), int(input())))


# Problem: Hybrid Sort
def hSort(li, dir):
    def oreum(li):
        def oneTimeSort(li, start_ind):
            end_ind = len(li) - start_ind
            for i in range(start_ind, end_ind - 1):
                if li[i] > li[i+1]:
                    li[i], li[i+1] = li[i+1], li[i]
            print(' '.join(list(map(str, li))))
            min_ind = li.index(min(li[start_ind:end_ind]))
            li[start_ind], li[min_ind] = li[min_ind], li[start_ind]
            return li
        start_ind = 0
        end_ind = len(li) - 1
        while start_ind < end_ind:
            li = oneTimeSort(li, start_ind)
            print(' '.join(list(map(str, li))))
            start_ind += 1
            end_ind -= 1
        return li
    
    def naerim(li):
        def oneTimeSort(li, start_ind):
            end_ind = len(li) - start_ind
            for i in range(start_ind, end_ind - 1):
                if li[i] < li[i+1]:
                    li[i], li[i+1] = li[i+1], li[i]
            print(' '.join(list(map(str, li))))
            max_ind = li.index(max(li[start_ind:end_ind]))
            li[start_ind], li[max_ind] = li[max_ind], li[start_ind]
            return li
        start_ind = 0
        end_ind = len(li) - 1
        while start_ind < end_ind:
            print(' '.join(list(map(str, li))))
            li = oneTimeSort(li, start_ind)
            start_ind += 1
            end_ind -= 1
    
    if dir == "오름차순":
        return oreum(li)
    elif dir == "내림차순":
        return naerim(li)

li = list(map(int, input().split()))
dir = input()
a = hSort(li, dir)


# Problem: Sorting Coordinates
n = int(input())
coord_list = []
for i in range(n):
    coord_list.append(list(map(int, input().split())))

def coordSort(li):
    coordsort_list = []
    while len(li) != 0:
        inspection_list = []
        M = min([i[0] for i in li])
        for l in li:
            if l[0] == M:
                inspection_list.append(l)
        if len(inspection_list) != 1:
            M_local = min([i[1] for i in inspection_list])
            coordsort_list.append([inspection_list[0][0], M_local])
            li.remove([inspection_list[0][0], M_local])
        else:
            coordsort_list.append(inspection_list[0])
            li.remove(inspection_list[0])
    return coordsort_list

l = coordSort(coord_list)
for i in l:
    print(' '.join(list(map(str, i))))
