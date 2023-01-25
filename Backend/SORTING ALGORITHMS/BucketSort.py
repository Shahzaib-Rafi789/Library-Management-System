from math import floor
import math
import AuxiliaryFunctions as Afunc
import CountingSort as CountSt
import RadixSort as RadixSt

def BucketSortIntegerInc(Input):
    BucketNo = 10
    max = Afunc.FindMax(Input)
    min = Afunc.FindMin(Input)

    Buckets = [None] * BucketNo
    range = max - min
    Size = floor(range / 10) if math.ceil(range/10) * 10 - range < math.ceil(range/10) else math.ceil(range/10)

    for i in Input:
        index = int((i - min) / Size)
        index = index if index < BucketNo else BucketNo - 1

        if(Buckets[index] == None):
            Buckets[index] = list()

        Buckets[index].append(i)

    index = 0
    for Bucket in Buckets:
        if(Bucket != None):
            Bucket = CountSt.CountingSortAsc(Bucket)
            Input[index: index + len(Bucket)] = Bucket
            index +=  len(Bucket)

    return Input


def BucketSortIntegerDec(Input):
    BucketNo = 10
    max = Afunc.FindMax(Input)
    min = Afunc.FindMin(Input)

    Buckets = [None] * BucketNo
    range = max - min
    Size = floor(range / 10) if math.ceil(range/10) * 10 - range < math.ceil(range/10) else math.ceil(range/10)

    for i in Input:
        index = int((i - min) / Size)
        index = index if index < BucketNo else BucketNo - 1
        index = (BucketNo - 1) - index

        if(Buckets[index] == None):
            Buckets[index] = list()

        Buckets[index].append(i)

    index = 0
    for Bucket in Buckets:
        if(Bucket != None):
            Bucket = CountSt.CountingSortDesc(Bucket)
            Input[index: index + len(Bucket)] = Bucket
            index +=  len(Bucket)

    return Input


def BucketSortStringInc(Input):
    BucketNo = 26
    Buckets = [None] * BucketNo

    for i in Input:
        index = 0
        if(i != ''):
            ascii = ord(i[0])
            index = ascii - 65 if ascii < 97 else ascii - 97

        if(Buckets[index] == None):
            Buckets[index] = list()

        Buckets[index].append(i)

    index = 0
    for Bucket in Buckets:
        if(Bucket != None):
            Bucket = RadixSt.RadixSortStringInc(Bucket)

            Input[index: index + len(Bucket)] = Bucket
            index +=  len(Bucket)

    return Input


def BucketSortStringDec(Input):
    BucketNo = 26
    Buckets = [None] * BucketNo

    for i in Input:
        index = 0
        if(i != ''):
            ascii = ord(i[0])
            index = ascii - 65 if ascii < 97 else ascii - 97
            index = BucketNo - 1 - index

        if(Buckets[index] == None):
            Buckets[index] = list()

        Buckets[index].append(i)

    index = 0
    for Bucket in Buckets:
        if(Bucket != None):
            Bucket = RadixSt.RadixSortStringDec(Bucket)

            Input[index: index + len(Bucket)] = Bucket
            index +=  len(Bucket)

    return Input


A = BucketSortStringDec(Afunc.RandomStrings(5000000))
print(Afunc.AreStringsInDecOrder(A))