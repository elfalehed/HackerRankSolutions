#! /usr/bin/env pypy3 

import os, sys

def solve(s):
    po = s.find(" ") 
    for i in s: 
        op = " "
        if s.find(op)!=0: 
            pp = s.find(" ") 
            s.replace(s[pp],"") 
            s.replace(s[pp],s[pp].upper())
        break 
    print(s)
    for i in s:
        if s.find(op)==0:
            st = s[0].upper()
            nd = s[po+1].upper() 
            rest = s[1:int(po)]
            rest1 = s[po+2:] 
            return(str(st) + rest + " " + str(nd) + rest1)
if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
