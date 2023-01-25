import funcs 
import time 




arr1=[10, 20, 80, 30, 60, 50,110, 100, 130, 170]
print(arr1)
arr2=[]
start=0
start_time=time.time()
found_idx=funcs.linear(arr1,len(arr1),130)
end_time=time.time()

runtime=end_time-start_time
print("The found idx is ", found_idx)
print("The runtime is",runtime)


