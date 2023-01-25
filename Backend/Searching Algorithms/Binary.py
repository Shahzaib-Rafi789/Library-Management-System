import funcs 
import time 




#arr1=funcs.RandomArray(100)
arr1=[1,2,3,4,5,6,7,8,9,10]
arr2=[]
start=0
start_time=time.time()
found_idx=funcs.binary(arr1,3)
end_time=time.time()

runtime=end_time-start_time
print("The found idx is ", found_idx)
print("The runtime is",runtime)


