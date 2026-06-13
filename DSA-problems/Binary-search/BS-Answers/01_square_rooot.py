'''Given a positive integer n. Find and return its square root. If n is not a perfect square, then return the floor value of sqrt(n).'''
n = 2
#brute tc=o(n), sc=0(1)
def brute(n):
    if n==0:
        return 0
    if n==1:
        return 1
    for i in range(2,n//2+2):
        if i**2==n:
            return i
        elif i**2>n:
            return i-1
print(brute(n))

def better(n):
    if n==0:
        return 0
    if n==1:
        return 1
    i=1
    while i*i<=n:
        i+=1
    return i-1
print(better(n))

def optimal(n):
    if n==0:
        return 0
    if n==1:
        return 1
    low=1
    high=n//2
    ans=-1
    while low<=high:
        mid=(low+(high-low)//2)
        if mid**2==n:
            return mid
        elif mid**2<n:
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans
print(optimal(n))