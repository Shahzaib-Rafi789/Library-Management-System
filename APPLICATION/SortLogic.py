from xml.dom.minidom import AttributeList
import SortingFuncs as SortF
import AuxiliaryFunctions as Afunc
from BookClass import Book
class ItemToSort:
    def __init__(self, item, key, StartingIndex):
        self.item = item
        self.key = key
        self.SIndex = StartingIndex


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


class SortFunc:
    def __init__(self, Identifier, IntName, StrName, int, string, IntInc, IntDec, StrInc, StrDec, ReduceValue):#Int and string name because some functions canot do both in one func. Two functions of different name r req.
        self.Identifier = Identifier
        self.IntFuncName = IntName
        self.StrFuncName = StrName
        self.CanSortInt = int
        self.CanSortString = string
        self.IntInc = IntInc
        self.IntDec = IntDec
        self.StrInc = StrInc
        self.StrDec = StrDec
        self.ReduceLenByOne = ReduceValue # decide whether to send len(A) or len(A) -1. Made for Quci Sort
        

    def GetName(self, type):
        if type == 'int':  return self.IntFuncName
        else: return self.StrFuncName   

    def CanSort(self, type):
        if type == 'int':  return self.CanSortInt
        return self.CanSortString    

    def GetOperator(self, order, attrType):
        if(attrType == "int"):
            if order == "Increasing" : return self.IntInc
            return self.IntDec
        
        else:
            if order == "Increasing" : return self.StrInc
            return self.StrDec


class AllSortFunc:
    SortingFuncLst = list()

    @staticmethod
    def AddFunc(Func):
        AllSortFunc.SortingFuncLst.append(Func)

    @staticmethod
    def GetFunc(FuncName):
        for i in AllSortFunc.SortingFuncLst:
            if i.Identifier == FuncName:
                return i
            
    @staticmethod
    def GetListAccToType(attrtype):
        print(attrtype,"subhan")
        lst = []
        for i in AllSortFunc.SortingFuncLst:
            lst.append(i.Identifier)     
        return lst


AllSortFunc.AddFunc(SortFunc("Insertion Sort", "InsertionSort", "InsertionSort", True, True, '<', '>','|<', '|>',0))
AllSortFunc.AddFunc(SortFunc("Bubble Sort", "BubbleSort", "BubbleSort", True, True, '<', '>','|<', '|>',0))
AllSortFunc.AddFunc(SortFunc("Selection Sort", "SelectionSort", "SelectionSort", True, True, '<', '>','|<', '|>',0))
AllSortFunc.AddFunc(SortFunc("Comb Sort", "CombSort", "CombSort", True, True, '>', '<','|>', '|<',0))#opposite symbols
AllSortFunc.AddFunc(SortFunc("Shell Sort", "ShellSort", "ShellSort", True, True, '>', '<','|>', '|<',0))#opposite symbols
AllSortFunc.AddFunc(SortFunc("Strand Sort", "StrandSort", "StrandSort", True, True, '<', '>','|<', '|>',0))
AllSortFunc.AddFunc(SortFunc("Merge Sort", "MergeSort", "MergeSort", True, True, '<=', '=>','|<=', '|>=',0))
AllSortFunc.AddFunc(SortFunc("Hybrid Merge Sort", "HybridMergeSort", "HybridMergeSort", True, True, '<', '>','|<', '|>',0))
AllSortFunc.AddFunc(SortFunc("Quick Sort", "QuickSort", "", True, False, '<', '>','|<', '|>',1))# 1 at end decide whether to send len(A) or len(A) -1. Made for Quci Sort
AllSortFunc.AddFunc(SortFunc("Counting Sort", "CountingSort", "CountingSort", True, False, '<', '>','|<', '|>',0))
AllSortFunc.AddFunc(SortFunc("Pigeon Hole Sort", "PigeonHoleSort", "PigeonHoleSort", True, False, '<', '>','|<', '|>',0))


class SortClass:
    def __init__(self, UnsortedLst, FuncName,attribute, Order, attrType, StartingIndex):#here op can be <,>,<= etc.
        self.UnsortedLst = UnsortedLst
        self.FuncForSort = FuncName
        self.attribute = attribute
        self.SortingOrder = Order
        self.attributeList = [ItemToSort(self.UnsortedLst[i].__getattribute__(self.attribute),i, StartingIndex) for i in range(len(self.UnsortedLst))]
        self.attrType = attrType

    def Sort(self):
        Func = AllSortFunc.GetFunc(self.FuncForSort)#Generically get function by its name
        if not Func.CanSort(self.attrType):
            return self.attributeList # Unsorted
        
        FuncName = Func.GetName(self.attrType)
        ReduceLen = Func.ReduceLenByOne # decide whether to send len(A) or len(A) -1. Made for Quci Sort

        output_function = getattr(SortF, FuncName)#gets func name i.e. insertion sort, merge sort etc
        return output_function(self.attributeList, 0, len(self.attributeList) - ReduceLen, Func.GetOperator(self.SortingOrder, self.attrType)) #pass parameters to functions , sorts and return sorted array


class SortHandler:
    def __init__(self, levels, Instructions):
        self.Levels = levels
        self.Executions = list()
        for i in Instructions:
            self.Executions.append(i)

    def SortingExecution(self):
        InstructionSet = self.Executions[0]

        SingleLevelSorting = SortClass(InstructionSet[0], InstructionSet[1], InstructionSet[2], InstructionSet[3], InstructionSet[4], 0)
        SortedArr = SingleLevelSorting.Sort()
        NewArr = self.MakeChangesToLst(SortedArr, InstructionSet[0])
        print(len(NewArr),'fgcfcf')
        MultiSortingWRT = [] #stores columns acc to which multi sorting is to be done 
        Attrs = []
        for level in range(1, self.Levels):
            InstructionSet = self.Executions[level]

            tuples = [self.Executions[i][2] for i in range(0,level)]
            MultiSortingWRT = self.GetCorrespendingIndexes(NewArr, tuples, InstructionSet[2])
            
            for i in MultiSortingWRT:
                MultiLevelSorting = SortClass(i[0], InstructionSet[1], InstructionSet[2], InstructionSet[3], InstructionSet[4], i[1])
                SortedArr = MultiLevelSorting.Sort()
                NewArr = self.MakeChangesToLst(SortedArr, NewArr)
        
        return NewArr
    
    def GetCorrespendingIndexes(self, Input, tuples, att):
        prev = [Input[0].__getattribute__(tuples[j]) for j in range(len(tuples))]
        OccurenceCount, SIndex, iteration = 1, 0, 0
        returnList, tempList = [], []
        tempList.append(Input[0])

        for i in range(1, len(Input)):
            Current = [Input[i].__getattribute__(tuples[j]) for j in range(len(tuples))]

            if(prev == Current):
                if OccurenceCount == 1: 
                    SIndex = iteration
                    if iteration == 0: OccurenceCount+=1
                tempList.append(Input[i])
                OccurenceCount +=1

            else:
                if OccurenceCount > 1:returnList.append((tempList, SIndex))
                OccurenceCount = 1
                tempList = []
                tempList.append(Input[i])
                prev = Current

            iteration += 1

        if OccurenceCount > 1:
            returnList.append((tempList, SIndex))

        return returnList

    def MakeChangesToLst(self, SortedLst, OldLst):
        NewLst = [OldLst[i] for i in range(len(OldLst))]
        NewLst[SortedLst[0].SIndex : SortedLst[0].SIndex + len(SortedLst)] = [OldLst[SortedLst[i].SIndex + SortedLst[i].key] for i in range(len(SortedLst))]
        
        return NewLst
    


def GenerateDummyBook():
    return Book(Afunc.RandomString(), Afunc.RandomString(), Afunc.RandomString(), Afunc.RandomNumber(), Afunc.RandomNumber(), Afunc.RandomString(), Afunc.RandomString(), Afunc.RandomNumber())

# print(AllSortFunc.GetListAccToType('string'))
# lst = [GenerateDummyBook() for i in range(25)]
# lst1 = [ItemToSort(lst[i].__getattribute__("edition"),i) for i in range(len(lst))]
# c = SortClass(lst, 'Insertion Sort', 'edition', 'Increasing', "int")
# c = SortHandler(2, [[lst, 'Pigeon Hole Sort', 'edition', 'Decreasing', "
# int"], [lst, 'Strand Sort', 'publisher', 'Increasing', "string"], [lst, 'Merge Sort', 'title', 'Increasing', "string"]])

# a = c.SortingExecution()
# b = [a[i].item for i in range(len(a))]
# print(Afunc.IsInIncOrder(b))

# nLst =[]
# def MakeChangesToLst(a, lst):
#     for i in range(len(a)):
#         nLst.append(lst[a[i].key])

# MakeChangesToLst(a, lst)

# print('\n\n')
# for i in lst:
#     print(i.title, '\t', i.publisher, '\t\\%\\%', i.edition)

# for i in a:
#     print(i.title, '\t', i.publisher, '\t\\%\\%', i.edition)
