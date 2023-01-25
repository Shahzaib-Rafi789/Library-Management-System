from operator import imod
import AuxiliaryFunctions as Afunc
import string
import random
import operator
from BookClass import Book
rel_ops = {
        '>': operator.gt,
        '>=': operator.ge,
        '<': operator.lt,
        '<=': operator.le,
        '==': operator.eq,
        '!=': operator.ne,
        '|<': Afunc.IsLess,
        '|>': Afunc.IsGreater,
        '|<=':Afunc.IsLessOrEqual,
        '|>=':Afunc.IsGreaterOrEqual
    }

def RandomString():
    alphabets = string.ascii_lowercase + string.ascii_uppercase
    while True:
        str = ''.join(random.choice(alphabets) for i in range(random.randint(0,7)))
        if(str != ''):
            break

    return str


def RandomNumber():
    return random.randint(0,100000)     


class ItemToSort:
    def __init__(self,item,key):
        self.item = item
        self.key = key


# class Book:
#     def __init__(self,title,authors,language,pages,edition,publisher,publishYear,isbn):
#         self.title=title
#         self.authors=authors
#         self.language=language
#         self.pages=pages
#         self.edition=edition
#         self.publisher = publisher
#         self.publishYear=publishYear
#         self.isbn=isbn


def GenerateDummyBook():
    return Book(RandomString(), RandomString(), RandomString(), RandomNumber(), RandomNumber(), RandomString(), RandomString(), RandomNumber())

    
def CountingSort(DataStruct, start, end, relate):
    Range = Afunc.FindMax([DataStruct[i].item for i in range(len(DataStruct))])
    # print(Range)
    SortedArray = [0 for element in range(end - start)] 
    SecondaryList = [0 for element in range(Range+1)]

    OrderDecide = 0
    if relate == '>=' or relate =='>':
        OrderDecide = len(SecondaryList) - 1

    for i in range(0,len(DataStruct)):
        SecondaryList[ abs(OrderDecide - DataStruct[i].item) ] = SecondaryList[ abs(OrderDecide - DataStruct[i].item)] + 1

    for i in range(1,Range+1):
        SecondaryList[i] += SecondaryList[i-1]

    i = len(DataStruct)-1
    while i >= 0:
        SortedArray[SecondaryList[ abs(OrderDecide - DataStruct[i].item) ]-1] = DataStruct[i]
        SecondaryList[ abs(OrderDecide - DataStruct[i].item) ] -= 1
        i -= 1
    
    return SortedArray      


def PigeonHoleSort(DataStruct, start, end, relate):
    Data = [DataStruct[i].item for i in range(len(DataStruct))]
    min = Afunc.FindMin(Data)
    max = Afunc.FindMax(Data)
    Range = max - min
    PigeonHoles = [0 for element in range(end - start)] 
    CounterList = [0 for element in range(Range+1)]
    temp = min if relate == '<' or relate == '<=' or relate =='|<' else max

    for i in range(0,len(DataStruct)):
        CounterList[abs( DataStruct[i].item - temp)] = CounterList[abs( DataStruct[i].item - temp)] + 1

    for i in range(1,Range+1):
        CounterList[i] += CounterList[i-1]

    i = len(DataStruct)-1
    while i >= 0:
        PigeonHoles[CounterList[abs( DataStruct[i].item - temp)]-1] = DataStruct[i]
        CounterList[abs( DataStruct[i].item - temp)] -= 1
        i -= 1    

    for i in range(len(PigeonHoles)):
        DataStruct[i] = PigeonHoles[i]

    return DataStruct


def InsertionSort(array, start, end, relate):
    for i in range(start+1, end):
        key = array[i].item
        key1 = array[i].key
        j = i-1
        
        while(rel_ops[relate](key, array[j].item) and j >= start ): # rel_ops is a dict and we are acessing built in comparsion operators using key
            array[j+1].item = array[j].item
            array[j+1].key =  array[j].key
            j = j - 1
    
        array[j+1].item = key
        array[j+1].key = key1
        
    return array

    
def SelectionSort(array, start, end, relate):
    i = start
    for i in range(end-1):
        extreme_index = Afunc.GetMinsIndex([array[i].item for i in range(len(array))], i, len(array)) if relate == '<' or relate =='|<' else Afunc.GetMaxsIndex([array[i].item for i in range(len(array))], i, len(array))
        array[i], array[extreme_index] = array[extreme_index], array[i]

    return array


def BubbleSort(array, start, end, relate):
    for i in range(start, end):
        for j in range(i+1, end):

            if (not rel_ops[relate](array[i].item, array[j].item)): # relate here can be <= or >= but not < or > to make alg stable
                array[i], array[j] = array[j], array[i]

    return array


# def CombSort(arr, relate):
    offset = len(arr)
    swap = True
    i = 0

    while offset > 1 or swap:
        offset = offset // 1.3
        offset = int(offset)
        swap = False
        i = 0

        while offset + i < len(arr):
            if rel_ops[relate](arr[i].item, arr[offset+i].item):
                arr[i], arr[offset+i] = arr[offset+i], arr[i]
                swap = True
            i += 1
    return arr


def ShellSort(arr, start, end, relate):
    offset = end//2

    while (offset > 0):

        for i in range(offset, end):
            pivot = arr[i].item
            j = i
            while (j >= offset and rel_ops[relate](arr[j-offset].item , pivot)):
                arr[j], arr[j-offset] = arr[j-offset], arr[j]
                j = j-offset
                arr[j].item = pivot
        offset = offset//2

    return arr


def MergeSort(array, start, end, relate):

    if (len(array) > 1):
        mid = (start + end) // 2
        L = array[0:mid]
        R = array[mid:len(array)]

        MergeSort(L, 0, len(L), relate)
        MergeSort(R, 0, len(R), relate)

        i = j = k = 0

        while (i < len(L) and j < len(R)):
            if (rel_ops[relate](L[i].item, R[j].item)):
                array[k] = L[i]
                i = i+1
            else:
                array[k] = R[j]
                j = j+1

            k = k+1

        while (i < len(L)):
            array[k] = L[i]
            i = i+1
            k = k+1

        while (j < len(R)):
            array[k] = R[j]
            j = j+1
            k = k+1

    return array


def HybridMergeSort(array, start, end, relate):

    arr = []
    l = len(array)

    if (l <= 0):
        return
    else:
        mid = l//2
        p = [None] * mid
        q = [None] * mid
        k = 0
        for i in range(start, mid):
            p[i] = array[i]
        for j in range(mid, end):
            q[k] = array[j]
            if (k < (len(q) - 1)):
                k = k+1

    lsize = len(p)
    rsize = len(q)
    i = 0
    j = 0
    while (i < lsize and j < rsize):
        if rel_ops[relate](p[i].item, q[j].item):
            arr.append(p[i])
            i = i+1
        else:
            arr.append(q[j])
            j = j+1

    while (i < lsize):
        arr.append(p[i])
        i = i+1

    while (j < rsize):
        arr.append(q[j])
        j = j+1

    sortedarr = InsertionSort(arr, 0, len(arr),relate)
    return sortedarr


def QuickSort(arr,start,end,relate):

    if(start<end):
        pivot=partition(arr,start,end,relate)
        QuickSort(arr,start,pivot-1,relate)
        QuickSort(arr,pivot+1,end,relate)

    return arr


def partition(arr,start,end,relate):
    #pivot=arr[random.randint(start, end-1)]
    pivot=arr[end].item
    i=start-1
    j=start
    for j in range(start,end):
        if(rel_ops[relate](arr[j].item, pivot)):
            i+=1
            (arr[i], arr[j]) = (arr[j], arr[i])
    
    i+=1
    arr[i], arr[end] = arr[end], arr[i]

    return i


def Strand(arr, relate):
    i=0
    if relate[-1] != '=': relate+='='
    subarr =[arr.pop(0)]
    while (i < len(arr)):
        if (not rel_ops[relate](arr[i].item, subarr[-1].item)):
            subarr.append(arr.pop(i))
        else:
            i += 1

    return subarr


def Strandmerge(subarr, final_arr, relate):

    output_arr = []
    while (len(subarr) and len(final_arr)):
        if (rel_ops[relate](subarr[0].item, final_arr[0].item)):
            output_arr.append(subarr.pop(0))
        else:
            output_arr.append(final_arr.pop(0))
    output_arr += subarr
    output_arr += final_arr

    return output_arr


def StrandSort(array, start, end, relate):
    f_array = Strand(array, relate)
    while(len(array)):
        f_array = Strandmerge(f_array, Strand(array, relate), relate)

    return f_array


def CombSort(arr, start, end, relate):
    offset = end
    swap = True
    i = 0

    while offset > 1 or swap:
        offset = int(offset / 1.3)
        if offset < 1: offset = 1
        # offset = int(offset)
        swap = False
        i = 0

        while offset + i < end:
            if rel_ops[relate](arr[i].item, arr[offset+i].item):
                (arr[i], arr[offset+i]) = (arr[offset+i], arr[i])
                swap = True
            i += 1
    return arr

# A = Afunc.RandomArray(20)
# print(A)
# print('\n\n',StrandSort(A))

# for aa in range(100):
# lst = [GenerateDummyBook() for i in range(1000000)]
# lst1 = [ItemToSort(lst[i].__getattribute__("edition"),i) for i in range(len(lst))]
# # lst1 = [ItemToSort(lst[i].__getattribute__("publisher"),i) for i in range(len(lst))]

# a = PigeonHoleSort(lst1, 0,len(lst1), '>')
# b = [a[i].item for i in range(len(a))]
# print(Afunc.IsInDecOrder(b))

# nLst =[]
# def MakeChangesToLst(a, lst):
#     for i in range(len(a)):
#         nLst.append(lst[a[i].key])

# # MakeChangesToLst(a, lst)
# for i in b:
#     print(i)

# print('abx' < 'abY')