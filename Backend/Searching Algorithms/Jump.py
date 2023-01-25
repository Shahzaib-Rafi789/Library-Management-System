import funcs 
import time 




#arr1=funcs.RandomArray(100)
arr1=[0, 1, 1, 2, 3, 5, 8, 13, 21,34, 55, 89, 144, 233, 377, 610]
start=0
start_time=time.time()
found_idx=funcs.jump(arr1,55,len(arr1))
end_time=time.time()

runtime=end_time-start_time
print("The found idx is ", found_idx)
print("The runtime is",runtime)


