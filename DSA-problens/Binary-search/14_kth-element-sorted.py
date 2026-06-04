'''Given two sorted arrays a and b of size m and n respectively. Find the kth element of the final sorted array.'''
a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
k = 5
#1,2,3,4,6,
# 7,8,9,10
#  1,4 | 8,10
#2,3,6 | 7,9

#brute force=> merge arrays and store it in an array
#TC= O(m+n) SC=O(m+n)

#better TC=O(m+n) SC=O(1)
#Optimize space complexity by not storing values in array
def better(a,b,k):
    n1=len(a)
    n2=len(b)
    i=0
    j=0
    count=1
    el=-1
    while i<n1 and j<n2:
        if a[i]<b[j]:
            if count==k:
                el=a[i]
            i+=1    
        else:
            if count==k:
                el=b[j]
            j+=1
        count+=1
    while i<n1:
        if count==k:
            el=a[i]
        count+=1
        i+=1
    while j<n2:
        if count==k:
            el=b[j]
        count+=1
        j+=1 
    return el
print(better(a,b,k))

#TC = O(log(min(n1​,n2​))) SC= O(1)
def optimal(a,b,k):
    n1=len(a)
    n2=len(b)
    if n1>n2:
        return optimal(b,a,k)
    low = max(0, k - n2)
    high = min(k, n1)
    while low<=high:
        mid1=(low+high)//2
        
        mid2=k-mid1
        
        l1=float('-inf')
        l2=float('-inf')
        
        r1=float('inf')
        r2=float('inf')
        
        if (mid1< n1):
            r1=a[mid1]
        if (mid2 < n2):
            r2=b[mid2]
            
        if (mid1-1 >=0):
            l1=a[mid1-1]
        if(mid2-1 >=0):
            l2=b[mid2-1]
            
        if l1<=r2 and l2<=r1:
            return max(l1,l2)
                
        elif l1>r2:
            high=mid1-1
        else:
            low=mid1+1
            
print(optimal(a,b,k))
            
                