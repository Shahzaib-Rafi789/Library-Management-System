import AuxiliaryFunctions as Afunc
import time

def RadixSortIntegerInc(Input):
    NoOfDigits = len( str(Afunc.FindMax(Input)) )

    for i in range(NoOfDigits):
        Buckets = [None] * 10

        #Create a Bucket and then check place value i of every element where i value is decreasing after every outerloop iteration.
        for value in Input:
            index = int(( value % pow(10, i+1) ) / pow(10, i)) 
            if(Buckets[index] == None):    
                Buckets[index] = list()

            Buckets[index].append(value)

        #Places value from Bucket to the Argument array in the order they are placed in bucket.
        index = 0
        for lists in Buckets:
            if(lists != None):
                Input[index: index + len(lists)] = lists
                index +=  len(lists)
    
    return Input


def RadixSortIntegerDec(Input):
    NoOfDigits = len( str(Afunc.FindMax(Input)) )
    Radix = 10

    for i in range(NoOfDigits):
        Buckets = [None] * Radix

        for value in Input:
            index = (Radix - 1) - int(( value % pow(10, i+1) ) / pow(10, i)) # To get Answer in descending order. if place value is 3 then it will be place at 9-3 = 7
            if(Buckets[index] == None):    
                Buckets[index] = list()

            Buckets[index].append(value)

        index = 0
        for lists in Buckets:
            if(lists != None):
                Input[index: index + len(lists)] = lists
                index +=  len(lists)
    
    return Input


def RadixSortStringInc(Input):
    NoOfChar= Afunc.FindMostDigitstring(Input)
    Radix = 26

    for i in range(NoOfChar-1,-1,-1):
        Buckets = [None] * (2 * Radix)

        for str in Input:
            index = 0
            if(i < len(str)):
                ascii = ord(str[i])
                index = (ascii - 65) if ascii < 97 else (ascii - 97) + Radix

            if(Buckets[index] == None):    
                Buckets[index] = list()

            Buckets[index].append(str)

        for i in range(Radix - 1):
            temp = Buckets[i + Radix]
            Buckets.pop(i + Radix)
            Buckets.insert( i *2 + 1, temp)


        index = 0
        for lists in Buckets:
            if(lists != None):
                Input[index: index + len(lists)] = lists
                index +=  len(lists)
    
    return Input


def RadixSortStringDec(Input):
    NoOfChar= Afunc.FindMostDigitstring(Input)
    Radix = 26

    for i in range(NoOfChar-1,-1,-1):
        Buckets = [None] * (2 * Radix)

        for str in Input:
            index = 0
            if(i < len(str)):
                ascii = ord(str[i])
                index = (ascii - 65) if ascii < 97 else (ascii - 97) + Radix

            index = (Radix * 2 - 1) - index 
            if(Buckets[index] == None):    
                Buckets[index] = list()

            Buckets[index].append(str)
        

        for i in range(Radix - 1):
            temp = Buckets[i + Radix]
            Buckets.pop(i + Radix)
            Buckets.insert( i *2 + 1, temp)


        index = 0
        for lists in Buckets:
            if(lists != None):
                Input[index: index + len(lists)] = lists
                index +=  len(lists)
    
    return Input

t = time.time()
A = RadixSortIntegerInc(Afunc.RandomArray(1000000))
print(Afunc.IsInIncOrder(A), sep = '\n')
print(time.time() - t)

t = time.time()
A = RadixSortIntegerDec(Afunc.RandomArray(1000000))
print(Afunc.IsInDecOrder(A), sep = '\n')
print(time.time() - t)

t = time.time()
A = RadixSortStringInc(Afunc.RandomStrings(1000000))
print(Afunc.AreStringsInIncOrder(A), sep = '\n')
print(time.time() - t)

t = time.time()
A = RadixSortStringDec(Afunc.RandomStrings(1000000))
print(Afunc.AreStringsInDecOrder(A), sep = '\n')
print(time.time() - t)