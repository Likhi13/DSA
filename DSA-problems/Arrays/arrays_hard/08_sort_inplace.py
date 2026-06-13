''' You are given two integer arrays nums1 and nums2, 
sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function,
but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.'''

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
# TC=O(N)+O(N+M)^2, SC=O(1)
def brute(arr1,m,arr2,n):
    i=m+n-1
    j=n-1
    total=m+n
    while i>=m:
        arr1[i]=arr2[j]
        i-=1
        j-=1
    for i in range(m+n):
        for j in range(i+1,m+n):
            if arr1[i]>=arr1[j]:
                arr1[i],arr1[j]=arr1[j],arr1[i]

    return arr1
# print(brute(nums1,m,nums2,n))


# We write only to empty slots
# We move from right to left
# Elements to the left are never overwritten before they’re compared

# INTUITION: Place the largest remaining element into the last free position of nums1.
# TC= O(N+M), SC=O(1)
def optimal(arr1,m,arr2,n):
    i=m-1
    j=n-1
    k=m+n-1
    while j<=0:
        if i>=0 and arr1[i]>arr2[j]:
            arr1[k]=arr1[i]
            i-=1
        else:
            arr2[k]=arr2[j]
            j-=1
        k-=1
    return arr1
# print(optimal(nums1,m,nums2,n))

# ------------------------------------------------------------------------------------

# Striver's 3 versions

# TC= O(N+M)+O(N+M)-----SC=O(N+M)
def brute1(arr1,m,arr2,n):
    arr3=[0]*(n+m)
    index=0
    l=0
    r=0
    while l<m and r<n:
        if arr1[l]<=arr2[r]:
            arr3[index]=arr1[l]
            l+=1
            index+=1
        else:
            arr3[index]=arr2[r]
            r+=1
            index+=1
    while l<m:
        arr3[index]=arr1[l]
        index+=1
        l+=1
    while r<n:
        arr3[index]=arr2[r]
        index+=1
        r+=1
    # print(arr3)
    for i in range(m+n):
        arr1[i]=arr3[i]
    return arr1          
    
# print(brute1(nums1,m,nums2,n))
# TC=O((M+N)LOG(M+N)) -- SC=O(M+N)
def better(arr1,m,arr2,n):
    l=m-1
    r=0
    while l>=0 and r<n:
        if arr1[l]>=arr2[r]:
            arr1[l],arr2[r]=arr2[r],arr1[l]
            l-=1
            r+=1
        else:
            break
    for i in range(m,m+n):
        arr1[i]=arr2[m-i]
    return sorted(arr1)
    
# print(better(nums1,m,nums2,n)) 

# tc= = O((m + n) log(m + n)) sc=o(1)
def optimal1(arr1,m,arr2,n):
    t=m+n
    gap=t//2+(t%2)
    while gap>0:
        l=0
        r=l+gap
        while(r<t):
            # arr1 n arr2
            if l<m and r>=m:
                if arr1[l]>arr2[r-m]:
                    arr1[l],arr2[r-m]=arr2[r-m],arr1[l]
            # arr2 and arr2
            elif l>=m and r>=m:
                if arr2[l-m]>arr2[r-m]:
                    arr2[l-m],arr2[r-m]=arr2[r-m],arr2[l-m]
            # arr1 and arr1
            else:
                if arr1[l]>arr1[r]:
                    arr1[l],arr1[r]=arr1[r],arr1[l]
            l+=1
            r+=1
        if gap!=1:
            gap=gap//2 + (gap%2)
        else:
            break
    for i in range(m,m+n):
        arr1[i]=arr2[i-m]
        
    return arr1         
        
print(optimal1(nums1,m,nums2,n))
