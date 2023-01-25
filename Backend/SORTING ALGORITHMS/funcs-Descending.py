import random
import numpy as np


def RandomArray(size):
    arr = []
    for i in range(size):
        arr.append(random.randint(1, 10))

    return arr


def InsertionSort(array, start, end):
    i = start+1
    for i in range(i, end):
        temp = array[i]
        j = i-1
        while (array[j] < temp and j >= 0):
            array[j+1] = array[j]
            j = j-1
            array[j+1] = temp

    return array


def Maximum(Arr, starting, ending):
    max = Arr[starting]
    index = starting
    for i in range(starting, ending):
        if (Arr[i] > max):
            max = Arr[i]
            index = i

    return index


def SelectionSort(array, start, end):
    i = start
    for i in range(len(array)-1):
        min_index = Maximum(array, i, len(array))
        temp = array[i]
        array[i] = array[min_index]
        array[min_index] = temp

    return array


def BubbleSort(array, start, end):
    for i in range(start, end):
        for j in range(i+1, end):
            if (array[i] < array[j]):
                temp = array[i]
                array[i] = array[j]
                array[j] = temp

    return array


def ShuffleArray(array, start, end):
    for i in range(start, end):
        temp = array[i]
        rng_index = random.randint(start, end)
        array[i] = array[rng_index]
        array[rng_index] = temp

    return array


def HybridMergeSort(array, start, end):

    arr = []
    l = len(array)

    if (l <= 0):
        return
    else:
        mid = l//2
        p = np.empty(mid)
        q = np.empty(mid)
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
        if (p[i] > q[j]):
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

    sortedarr = InsertionSort(arr, 0, len(arr))
    return sortedarr


def MergeSort(array, start, end):

    if (len(array) > 1):
        mid = (start + end) // 2
        L = array[0:mid]
        R = array[mid:len(array)]

        MergeSort(L, 0, len(L))
        MergeSort(R, 0, len(R))

        i = 0
        j = 0
        k = 0

        while (i < len(L) and j < len(R)):
            if (L[i] >= R[j]):
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


def CombSort(arr):
    offset = len(arr)
    swap = True
    i = 0

    while offset > 1 or swap:
        offset = offset // 1.3
        offset = int(offset)
        swap = False
        i = 0

        while offset + i < len(arr):
            if arr[i] < arr[offset+i]:
                temp = arr[i]
                arr[i] = arr[offset+i]
                arr[offset+i] = temp
                swap = True
            i += 1
    return arr


def ShellSort(arr):
    offset = len(arr)//2

    while (offset > 0):

        for i in range(offset, len(arr)):
            pivot = arr[i]
            j = i
            while (j >= offset and arr[j-offset] < pivot):
                temp = arr[j]
                arr[j] = arr[j-offset]
                arr[j-offset] = temp
                j = j-offset
                arr[j] = pivot
        offset = offset//2

    return arr




def Strand(arr):

    #while (len(arr) > 0):
    #    subarr = [arr.pop(0)]

    i=0
    subarr =[arr.pop(0)]
    while (i < len(arr)):
        if (arr[i] < subarr[-1]):
            subarr.append(arr.pop(i))
        else:
            i += 1

    return subarr


def Strandmerge(subarr, final_arr):

    output_arr = []
    while (len(subarr) and len(final_arr)):
        if (subarr[0] > final_arr[0]):
            output_arr.append(subarr.pop(0))
        else:
            output_arr.append(final_arr.pop(0))
    output_arr += subarr
    output_arr += final_arr

    return output_arr


def StrandSort(array):
    f_array = Strand(array)
    while(len(array)):
        f_array = Strandmerge(f_array, Strand(array))

    return f_array


def QuickSort(arr,start,end):

    if(start<end):
        pivot=partition(arr,start,end)
        QuickSort(arr,start,pivot-1)
        QuickSort(arr,pivot+1,end)

    return arr


def partition(arr,start,end):
    #pivot=arr[random.randint(start, end-1)]
    pivot=arr[end-1]
    i=start-1
    j=start
    for j in range(start,end):
        if(arr[j]>pivot):
            i+=1
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    
    i+=1
    temp=arr[i]
    arr[i]=arr[end-1]
    arr[end-1]=temp

    return i