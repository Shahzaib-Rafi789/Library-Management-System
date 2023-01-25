import random
import numpy as np
import math

def RandomArray(size):
    arr = []
    for i in range(size):
        arr.append(random.randint(1, 10))

    return arr

def linear(arr,n,x):
    for i in range(n):
        if(arr[i]==x):
            return i

    return -1


def binary(arr,x):
    start=0
    end=len(arr)-1

    while(start<=end):
        mid=start+(end-start)//2
        val=arr[mid]

        if(val<x):
            start=mid+1
        elif(val>x):
            end=mid-1
        else:
            return mid

    return -1

def jump(arr,x,n):
    i=0
    start=0
    end=int(math.sqrt(n))

    while(arr[end]<x and start<n):
        start=end
        end+=int(math.sqrt(n))
        if(end>n-1):
            end=n
            
    for i in range(start,end):
        if(arr[i]==x):
            return i

    return -1







            




