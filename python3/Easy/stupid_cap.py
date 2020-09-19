#! /usr/bin/env pypy3 

def solve(s):
    for i in range(len(s)): 
        if s[i]==" ":
            p = i 
            s.replace(s[i], "") 
            bg = s[i].upper()
            s.replace(s[i], str(bg))
            return s
if __name__=='__main__':
    s = input() 
    result = solve(s) 
    print("TheRes= " + result) 

