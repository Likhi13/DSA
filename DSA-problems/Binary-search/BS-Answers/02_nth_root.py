'''Given two numbers N and M, find the Nth root of M. The Nth root of a number M is defined as a number X such that when X is raised to the power of N, it equals M. If the Nth root is not an integer, return -1.'''
n=3,m=27

def optimal(n,m):
    if m==0:
        return 0
    if m==1:
        return 1
    low=1
    high=m//2

    while low<=high:
        mid=(low+(high-low)//2)
        if mid**n==m:
            return mid
        elif mid**n<m:
            low=mid+1
        else:
            high=mid-1
    return -1
print(optimal(n,m))