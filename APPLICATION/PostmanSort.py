import AuxiliaryFunctions as Afunc

#Postman works same as Radix but starts from opposite direction i.e. from MSB to LSB.
#in each main loop iteration it increases the number of index from a single it takes meaning at first iteration it creates 10 buckets
#and takes 1st element. In Second iteration, it takes 1 st and 2nd element thus creating 100 buckets. In third iteration, it takes the first three index of element so if an element is
#2345 it will take 234 and create 1000 buckets.

def PostmanSortIntegerInc(Input):#Starts from MSB of all elements to the LsB of the largest element of the largest
    NoOfDigits = Afunc.FindMostDigitsInt(Input)

    MainBuckets = [None] * 10
    MainBuckets[0] = list()# This location will hold the sorted array
    GetMainBuckets(Input, MainBuckets)#Initially put all elements into buckets corrrespending to their MSB bit
    
    BucketsList = [None] * 10
    for i in range(10):
        BucketsList[i] = MainBuckets[i]#operations will be perform on this BucketList temp list

    for i in range(1, NoOfDigits + 1):#One more iteration to make sure all elements of input are appended to 0 index of MainBuckets which is the answer
        for val in range(0, 10):
            if(BucketsList[val] != None):
                elem = 0

                Buckets = [None] * pow(10,i+1) # creating buckets
                for j in range(len(BucketsList[val])):
                    strValue = str(BucketsList[val][j])

                    if(Afunc.NumberOfDigits(BucketsList[val][j]) > i):
                        index = int(strValue[0:i+1])
                        if(Buckets[index] == None):    
                            Buckets[index] = list()

                        Buckets[index].append(BucketsList[val][j])
                        elem += 1
                    else:
                        MainBuckets[0].append(BucketsList[val][j])# if i increases the bits in elemnet

                index = 0
                BucketsList[val] = [None] * elem
                for lists in Buckets:
                    if(lists != None):
                        BucketsList[val][index: index + len(lists)] = lists
                        index +=  len(lists)
    
    return MainBuckets[0]


def PostmanSortIntegerDesc(Input):#Starts from MSB of all elements to the LsB of the largest element of the largest
    NoOfDigits = Afunc.FindMostDigitsInt(Input)

    MainBuckets = [None] * 10
    MainBuckets[0] = list()# This location will hold the sorted array
    GetMainBuckets(Input, MainBuckets)#Initially put all elements into buckets corrrespending to max minus their MSB bit
    
    BucketsList = [None] * 10
    for i in range(10):
        BucketsList[i] = MainBuckets[i]

    for i in range(1, NoOfDigits + 1):
        for val in range(0, 10):
            if(BucketsList[val] != None):
                elem = 0

                Buckets = [None] * pow(10,i+1)
                for j in range(len(BucketsList[val])):
                    strValue = str(BucketsList[val][j])

                    if(Afunc.NumberOfDigits(BucketsList[val][j]) > i):
                        index = int(strValue[0:i+1])

                        if(Buckets[index] == None):    
                            Buckets[index] = list()

                        Buckets[index].append(BucketsList[val][j])
                        elem += 1
                    else:
                        MainBuckets[0].insert(0,BucketsList[val][j])#Only this line changed to convert the previous sorting in increasing function to decreasing function

                index = 0
                BucketsList[val] = [None] * elem
                for lists in Buckets:
                    if(lists != None):
                        BucketsList[val][index: index + len(lists)] = lists
                        index +=  len(lists)
    
    return MainBuckets[0]


def PostmanSortStringInc(Input):
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


def PostmanSortStringDec(Input):
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


def GetMainBuckets(Input, MainBuckets):# For Postman Sort
    for value in Input:
        strValue = str(value)
        index = int(strValue[0])
        index = index

        if(MainBuckets[index] == None):    
            MainBuckets[index] = list()

        MainBuckets[index].append(value)
    