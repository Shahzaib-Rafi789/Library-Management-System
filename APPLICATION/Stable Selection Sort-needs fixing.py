
import sys
import time 


def SelectionSort(array, start, n):

    for i in range(0,n-1):
        min=i
        j=i+1
        for j in range(n):
            if(array[min]>array[j]):
                min=j

        key=array[min]

        while (min > i):
            array[min] = array[min - 1]
            min-=1

        array[i] = key

    return array




#arr1=funcs.RandomArray(10)
arr1=[ 4, 5, 3, 2, 4, 1]
print(arr1)
n = sys.getsizeof(arr1) // sys.getsizeof(arr1[0])
arr2=[]
start=0
start_time=time.time()
arr2=SelectionSort(arr1,start,n)
end_time=time.time()

runtime=end_time-start_time
print(arr2)
print("The runtime is",runtime)



with open('SortedSelectionSort.csv','w') as file:
    for i in range(start,len(arr2)):
        file.write(str(arr2[i]))
        file.write("\n")


