#! /usr/bin/env/ python3


def countFreq(pat, txt):
    M = len(pat)
    N = len(txt)
    res = 0
    # A loop to slide pat[] one by one 
    for i in range(N - M + 1):
        # For current index i, check 
        # for pattern match 
        j = 0
        while j < M:
            if (txt[i + j] != pat[j]):
                break
            j += 1
 
        if (j == M):
            res += 1
            j = 0
    return res

# Driver Code Function to print all sub strings 
#def subString(s, n): 
    # Pick starting point in outer loop 
    # and lengths of different strings for 
    # a given starting point 
   

   # Driver program to test above function 
#s = "abcd"; 
#subString(s,len(s)); 

# pick all of the vowels from a string
def pickv(s,l):
    for i in range(len(s)):
        if s[i] in vowels: 
            l.append(s[i]) 
    return ''.join(l) 

def subs(txt, startswith):
    for i in range(len(txt)):
        for j in range(1, len(txt) - i + 1):
            if txt[i].lower() in startswith.lower():
                yield txt[i:i + j]

s = 'BANANA'
vowels = 'AEIOU'
if __name__ == '__main__':
    s = input()
    l = [] 
    spt = 0
    kpt = 0 
    vowels = 'AEIOU'
    cons = 'BCDFGHJKLMNPQRSTVWXYZ'
    ll = sorted(subs(s,vowels))
    pp = sorted(subs(s,cons)) 
    for i in range(len(s)):
        spt = spt +  s.count(pp[i]) 
        kpt = kpt + s.count(ll[i])

    """
    if spt > kpt:
        print("ST: ", spt)
    else:
        print("KEV: ", kpt) 
    #az = subString(s,len(s))
    """
    for i in range(len(s)):
        print(ll[i])
    

    #txt = "dhimanman"
    #pat = "man" 
    #print(countFreq(pat, txt))
 
