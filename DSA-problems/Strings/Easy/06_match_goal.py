'''Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.'''

s = "abcde"
goal = "cdeab"
# TC= O(N^2)--SC=O(N)
def brute(s,goal):
    if len(s)!=len(goal):
        return False
    temp=list(s)
    match=False
    for k in range(len(s)):
        for i in range(len(s)):
            t=(i+k)%len(s)
            temp[i]=s[t]
        if "".join(temp)==goal:
            match=True
            break
        temp=list(s)
    return match
# print(brute(s,goal))

def rotate(s,k):
    n=len(s)
    k=k%n
    temp=list(s)
    reverse(temp,0,k-1) #left
    reverse(temp,k,n-1) #right
    reverse(temp,0,n-1) #total
    return temp  

def reverse(temp,left,right):
    while left<right:
        temp[left],temp[right]=temp[right],temp[left]
        left+=1
        right-=1
      
def compare(s,goal):
    if len(s)!=len(goal):
        return False
    match=False
    for k in range(0,len(s)+1):
        ans=rotate(s,k)
        if "".join(ans)==goal:
            match=True
            break
    return match
print(compare(s,goal))

def optimal(s,goal):
    if len(s)!=len(goal):
        return False
    if goal in s+s:
        return True
    else:
        return False
print(optimal(s,goal))

        