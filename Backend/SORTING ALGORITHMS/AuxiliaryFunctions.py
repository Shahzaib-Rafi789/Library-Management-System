
from multiprocessing.sharedctypes import Value
import random
import string
from unicodedata import digit

def IsLess(a, b):
    return a < b



def IsLessOrEqual(a, b):
    return a <= b



def IsGreater(a, b):
    return a > b


def IsGreaterOrEqual(a, b):
    return a >= b



def RandomNumber():
    return random.randint(0,10)     



def RandomString():
    alphabets = string.ascii_lowercase + string.ascii_uppercase
    while True:
        str = ''.join(random.choice(alphabets) for i in range(random.randint(1,1)))
        if(str != ''):
            break

    return str



def RandomStrings(size):
    alphabets = string.ascii_lowercase + string.ascii_uppercase
    arr = []

    for i in range(size):
        str = ''.join(random.choice(alphabets) for i in range(random.randint(0,7)))

        if(str == ''):
            i = i - 1
            continue
        else:
            arr.append(str)
    return arr



def RandomArray(size):
    Arr = []
    
    for i in range(size):
        num = random.randint(0,100000)
        Arr.append(num)
        
    return Arr



def FindMax(DataStruct):
    maxim = DataStruct[0]

    for value in DataStruct:
        if value > maxim:
            maxim = value

    return maxim



def FindMin(DataStruct):
    minim = DataStruct[0]
    for value in DataStruct:
        if value < minim:
            minim = value

    return minim



def NumberOfDigits(n):
    digits = 1
    while(int(n/10) != 0):
        n = int(n/10)
        digits += 1
    
    return digits



def FindMostDigitstring(Input): # Checks which string from the array of string has the most characters
    if(len(Input) != 0):
        Num = len(Input[0])
        for i in range(1, len(Input)):
            if Num < len(Input[i]):
                Num = len(Input[i])

        return Num
    
    return 0



def FindMostDigitsInt(Input): #return total number of digits in max nummber
    max = FindMax(Input)

    digits = 1
    while(int(max / 10) != 0):
        digits += 1
        max = int(max / 10)
    
    return digits



def PopExtraElement(input):
    while(input[-1] == 0):
        input.pop(-1)

    return input


def IsInIncOrder(Arr):
    for i in range(1, len(Arr)):
        if(Arr[i] < Arr[i-1]):
            return False

    return True


def GetMinsIndex(Arr, starting, ending):
    min = Arr[starting]
    index = starting
    for i in range(starting, ending):
        if (Arr[i] < min):
            min = Arr[i]
            index = i

    return index


def GetMaxsIndex(Arr, starting, ending):
    max = Arr[starting]
    index = starting
    for i in range(starting, ending):
        if (Arr[i] > max):
            max = Arr[i]
            index = i

    return index


def IsInDecOrder(Arr):
    for i in range(1, len(Arr)):
        if(Arr[i] > Arr[i-1]):
            return False

    return True

def AreStringsInIncOrder(Arr):
    for i in range(1, len(Arr)):
        # for j in range(min(len(Arr[i]), len(Arr[i-1]))):
        #     ascii1 = ord(Arr[i][j]) - 65 if ord(Arr[i][j]) < 97 else ord(Arr[i][j]) - 97
        #     ascii2 = ord(Arr[i-1][j]) - 65 if ord(Arr[i-1][j]) < 97 else ord(Arr[i-1][j]) - 97

        #     if((ascii1 > ascii2) or ((ascii1 == ascii2) and ord(Arr[i-1][j]) < ord(Arr[i][j]))):
        #         break

        #     if(ascii1 < ascii2):
        #         return False
        if Arr[i - 1] > Arr[i]:
            return False 

    return True

def AreStringsInDecOrder(Arr):
    for i in range(1, len(Arr)):
        # for j in range(min(len(Arr[i]), len(Arr[i-1]))):
        #     ascii1 = ord(Arr[i][j]) - 65 if ord(Arr[i][j]) < 97 else ord(Arr[i][j]) - 97
        #     ascii2 = ord(Arr[i-1][j]) - 65 if ord(Arr[i-1][j]) < 97 else ord(Arr[i-1][j]) - 97

        #     if((ascii1 < ascii2) or ((ascii1 == ascii2) and ord(Arr[i-1][j]) > ord(Arr[i][j]))):
        #         break

        #     if(ascii1 > ascii2):
        #         return False
        if Arr[i - 1] < Arr[i]:
            return False

    return True

def StartsWith(Pat, txt):
    txt = str(txt)
    Pat = str(Pat)

    if len(txt) < len(Pat):
        return False

    if txt[0:len(Pat)] == Pat:
        return True
    
    return False


def EndsWith(Pat, txt):
    txt = str(txt)
    Pat = str(Pat)

    if len(txt) < len(Pat):
        return False

    if txt[len(txt) - len(Pat) : ] == Pat:
        return True
    
    return False


def IsEqualTo(Pat, txt):
    txt, Pat = str(txt), str(Pat)

    if txt == Pat:
        return True

    return False

def IsNotEqualTo(Pat, txt):
    txt, Pat = str(txt), str(Pat)

    if txt != Pat:
        return True

    return False

# A = RandomArray(100)
# # print(A, FindMostDigitstring(A))
# # print("Z" < "a")
# print(FindMax(A))
# print(FindMostDigitInt(A))


