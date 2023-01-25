import random
import numpy as np
import math

d=256

def naive(txt,pat):
    patlen=len(pat)
    txtlen=len(txt)

    for i in range(txtlen-patlen+1):
        j=0

        while(j<patlen):
            if(txt[i+j]!=pat[j]):
                break
            j+=1
            
        if(j==patlen):
            print("pattern found at :",i)


def rabin(pat,txt,q):
    patlen=len(pat)
    txtlen=len(txt)
    p,t=0
    h=1


    for i in range(patlen-1):
        h=(h*d)%q
    
    for i in range(patlen):
        p=(d*p+ord(pat[i]))%q
        t=(d*t+ord(txt[i]))%q

    for i in range(txtlen-patlen+1):
        j=0
        
        if(p==t):
            while(j<patlen):
                if(txt[i+j]!=pat[j]):
                    break
                j+=1
                    
            if(j==patlen):
                print("pattern at ",str(i))

        if(i<txtlen-patlen):
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+patlen])) % q

            if(t<0):
                t+=q



                
def Booyerhorsepool(txt,pat):
    t=len(txt)
    p=len(pat)
    
    if(p>t):
        return -1
    
    matchtable=[p]*128
        
    for j in range(p-1):
        matchtable[ord(pat[j])]=p-j-1
        
    k=p-1
    
    while(k<t):
        j=p-1
        i=k
        while((j>=0) and (txt[i]==pat[j])):
            j-=1
            i-=1
            
        if(j<0):
            return i+1
    
        k+=matchtable[ord(txt[k])]
        
    return -1
    
  
    
                
                













            




