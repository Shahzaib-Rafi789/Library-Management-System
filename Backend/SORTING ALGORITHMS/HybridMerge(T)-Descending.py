import funcs 
import time 



arr1=funcs.RandomArray(1000)
print(arr1)
arr2=[]
start=0
start_time=time.time()
arr2=funcs.HybridMergeSort(arr1,start,len(arr1))
end_time=time.time()

runtime=end_time-start_time
print(arr2)
print("The runtime is",runtime)



with open('SortedHyrbridSort.csv','w') as file:
    for i in range(start,len(arr2)):
        file.write(str(arr2[i]))
        file.write("\n")
