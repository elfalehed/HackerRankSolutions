#! /usr/bin/env python3 

# You need to custom along with your challenge, Cause most of them are just tested locally. 

def swap_case(s): 
    ss = list(s) 
    for i in range(len(s)): 
        ss[i] = ss[i].swapcase() 

    return "".join(ss) 

s = input() 
print(swap_case(s)) 
