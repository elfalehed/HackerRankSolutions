#! /usr/bin/env python3 

a = input() 
b = input() 
c = input() 
n = input() 
print ([[x,y,z] for x in range(int(a) + 1) for y in range(int(b) + 1) for z in range(int(c) + 1) if x + y + z != int(n)])


