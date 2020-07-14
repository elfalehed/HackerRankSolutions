#! /usr/bin/env python3 

N,M = map(int, input().split()) 
for i in range(1, N, 2): 
    print((str('.|.')*i).center(M, '-')) 
print(str('WELCOME').center(M,'-'))
for i in range(N-2, -1, -2): 
    print ((str('.|.')*i).center(M, '-')) 






