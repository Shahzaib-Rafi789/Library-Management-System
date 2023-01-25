import AuxiliaryFunctions as Afunc

def PigeonHoleIntegerAsc(DataStruct):
    min = Afunc.FindMin(DataStruct)
    max = Afunc.FindMax(DataStruct)
    Range = max - min
    PigeonHoles = [0 for element in range(len(DataStruct))] 
    CounterList = [0 for element in range(Range+1)]
  
    for i in range(0,len(DataStruct)):
        CounterList[DataStruct[i] - min] = CounterList[DataStruct[i] - min] + 1

    for i in range(1,Range+1):
        CounterList[i] += CounterList[i-1]

    i = len(DataStruct)-1
    while i >= 0:
        PigeonHoles[CounterList[DataStruct[i] - min]-1] = DataStruct[i]
        CounterList[DataStruct[i] - min] -= 1
        i -= 1    

    for i in range(len(PigeonHoles)):
        DataStruct[i] = PigeonHoles[i]

    return DataStruct


def PigeonHoleIntegerDesc(DataStruct):
    min = Afunc.FindMin(DataStruct)
    max = Afunc.FindMax(DataStruct)
    Range = max - min
    PigeonHoles = [0 for element in range(len(DataStruct))] 
    CounterList = [0 for element in range(Range+1)]
  
    for i in range(0,len(DataStruct)):
        CounterList[max - DataStruct[i]] = CounterList[max - DataStruct[i]] + 1

    for i in range(1,Range+1):
        CounterList[i] += CounterList[i-1]

    i = len(DataStruct)-1
    while i >= 0:
        PigeonHoles[CounterList[max - DataStruct[i]]-1] = DataStruct[i]
        CounterList[max - DataStruct[i]] -= 1
        i -= 1    

    for i in range(len(PigeonHoles)):
        DataStruct[i] = PigeonHoles[i]

    return DataStruct

