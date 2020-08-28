#! /usr/bin/env python 3

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    d = []
    for i in range(len(arr)):
        d.append(arr[i]) 
    for num in range(len(d)): 
        if num in d: 
            d.remove(d[num]) 
    d.sort() 
    print(d[-2])






