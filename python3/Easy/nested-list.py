#! /usr/bin/env python3 

if __name__=='__main__': 
    num = int(input())
    g = []
    n = [] 
    ll = [] 
    student = [] 
    for i in range(num):
        name = input()
        score = input() 
        ll.append(name) 
        ll.append(score)
    student.append(ll) 
    print(student)
