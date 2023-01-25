import funcs 
import time 

txt = "ronaldo is not sui"
pat = "sui"

#txt = "abaaabcd"
#pat = "abc"

idx = funcs.Booyerhorsepool(txt,pat)
if(idx<0):
    print("String not found")
else:
    print("found at ", idx)