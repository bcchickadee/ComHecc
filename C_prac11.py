# C_prac11.ipynb
# Chapter 11 Exercises

# Problem: Student Name Search 1
stu_no = [62, 3, 17, 90, 46, 67, 11, 24, 33, 69]
stu_name = ['jin', 'su', 'young', 'sun', 'yejin', 'rang', 'bok','iyou', 'seok','seul']

def stuSearch(num):
    '''
    Searching for student name from student number, in separate lists
    '''
    i = 0
    while i < len(stu_no) and stu_no[i] != num:
        i += 1
    if i == len(stu_no):
        return "?"
    else:
        return stu_name[i]

num = int(input('Student Number: '))
print(stuSearch(num))


# Problem: Student Name Search 2
stu_dict={62: 'jin', 3: 'su', 17: 'young', 90: 'sun', 46: 'yejin', 67: 'rang', 11: 'bok', 24: 'iyou', 33: 'seok', 69: 'seul'}

def stuSearchDict(num):
    '''
    Searching for student name from student number, in dict
    '''
    key_list = list(stu_dict.keys())
    i = 0
    while i < len(key_list) and key_list[i] != num:
        i += 1
    if i == len(stu_no):
        return "?"
    else:
        return stu_dict[key_list[i]]
    
num = int(input('Student Number: '))
print(stuSearchDict(num))


# Problem: Calculating Same Ranks
scores=[61, 61, 63, 69, 69, 69, 69, 70, 70, 71, 71, 71, 73, 75, 77, 77, 79, 96, 97, 98]

def SameScore(li):
    samedict = {}
    for i in li:
        if i in samedict.keys():
            samedict[i] += 1
        else:
            samedict[i] = 1
    return samedict

print(f'동점딕셔너리: {SameScore(scores)}')


# Problem: Ceiling function w/ Binary Search
data=[4, 6, 9, 17, 23, 30, 36, 42, 44, 47, 50, 56, 56, 57, 62, 64, 68, 89, 90, 95]

def CeilBSearch(li, query, low = 0, high = -1):
    '''
    Ceiling function inside list w/ Binary Search
    '''
    if high == -1:
        high = len(data) - 1
    mid = (low + high) // 2
    if query > data[-1]:
        return -1
    if li[mid] == query:
        return li[mid]
    elif high == low:
        return li[high]
    else:
        if li[mid] < query:
            low = mid + 1
            return CeilBSearch(li, query, low, high)
        elif li[mid] > query:
            high = mid - 1
            return CeilBSearch(li, query, low, high)

query = float(input('Input Number: '))
if int(query) == query:
    query = int(query)
print(f'Ceil({query}) = {CeilBSearch(data, query)}')


# Problem: Floor function w/ Binary Search
data=[4, 6, 9, 17, 23, 30, 36, 42, 44, 47, 50, 56, 56, 57, 62, 64, 68, 89, 90, 95]

def FloorBSearch(li, query, low = 0, high = -1):
    '''
    Floor function inside list w/ Binary Search
    '''
    if high == -1:
        high = len(li) - 1
    mid = (low + high) // 2
    if data[0] > query:
        return -1
    elif data[-1] < query:
        return data[-1]
    elif li[mid] == query:
        return li[mid]
    elif low == high or high - low == 1:
        return li[low]
    else:
        if li[mid] > query:
            high = mid
        elif li[mid] < query:
            low = mid
        return FloorBSearch(li, query, low, high)

query = float(input('Input Number: '))
if int(query) == query:
    query = int(query)

print(f'Floor({query}) = {FloorBSearch(data, query)}')


# Problem: Grading Scores
from ast import literal_eval

def gradeBSearch(dic, query, low = 0, high = -1):
    '''
    Grading Students w/ Binary Search
    '''
    def grading(ind, total):
        '''
        Grades depending on index
        '''
        a = int(total * 0.3)
        b = int(total * 0.6)
        if ind + 1 > a:
            return "A"
        elif ind + 1 > b:
            return "B"
        else:
            return "C"
    if high == -1:
        high = len(dic) - 1
    mid = (low + high) // 2
    l = list(dic.values())
    if l[mid] == dic[query]:
        return grading(mid, len(dic))
    else:
        if l[mid] > dic[query]:
            high = mid - 1
        elif l[mid] < dic[query]:
            low = mid + 1
        return gradeBSearch(dic, query, low, high)

dic = literal_eval(input('Input Data: '))
# dic = {"지형":55,"윤수":56,"윤호":58,"재우":60,"선우":62,"가희":65,"나희":68,"다희":71,"라희":74,"마희":75,"바희":78,"사희":82,"아희":86,"자희":90}
name = input('Student Name: ')
print(gradeBSearch(dic, name))


# Problem: Cutting Trees
tgt = int(input('Input M: '))
trees = list(map(int, input('Input tree length: ').split()))

cut = max(trees)
def cutlength(treelist, cutheight):
    wood = 0
    for i in treelist:
        if i > cutheight:
            wood += (i - cutheight)
    return wood

while cutlength(trees, cut) != tgt:
    cut -= 1
print(f'Height: {cut}')