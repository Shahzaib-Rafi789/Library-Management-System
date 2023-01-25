import AuxiliaryFunctions as Afunc


def CountingSortAsc(DataStruct):
    Range = Afunc.FindMax(DataStruct)
    SortedArray = [0 for element in range(len(DataStruct))] 
    SecondaryList = [0 for element in range(Range+1)]
  
    for i in range(0,len(DataStruct)):
        SecondaryList[DataStruct[i]] = SecondaryList[DataStruct[i]] + 1

    for i in range(1,Range+1):
        SecondaryList[i] += SecondaryList[i-1]

    i = len(DataStruct)-1
    while i >= 0:
        SortedArray[SecondaryList[DataStruct[i]]-1] = DataStruct[i]
        SecondaryList[DataStruct[i]] -= 1
        i -= 1
    
    return SortedArray


def CountingSortDesc(DataStruct):
    Range = Afunc.FindMax(DataStruct)
    SortedArray = [0 for element in range(len(DataStruct))] 
    SecondaryList = [0 for element in range(Range+1)]
  
    for i in range(0,len(DataStruct)):
        SecondaryList[len(SecondaryList) - DataStruct[i] - 1] = SecondaryList[len(SecondaryList) - DataStruct[i] - 1] + 1

    for i in range(1,Range+1):
        SecondaryList[i] += SecondaryList[i-1]

    i = len(DataStruct)-1
    while i >= 0:
        SortedArray[SecondaryList[len(SecondaryList) - DataStruct[i] - 1]-1] = DataStruct[i]
        SecondaryList[len(SecondaryList) - DataStruct[i] - 1] -= 1
        i -= 1
    
    return SortedArray

