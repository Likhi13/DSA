'''Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).'''
nums1 = [1,3,7,13]
nums2 = [2,3,11]

#brute, TC=O(m+n) SC=O(m+n)
#merge sorted arrays and calculate median
def merge(nums1,nums2):
    i=0
    j=0
    k=0
    arr=[0]*(len(nums1)+len(nums2))
    while i<len(nums1) and j <len(nums2):
        if nums1[i]<=nums2[j]:
            arr[k]=nums1[i]
            i+=1
        else:
            arr[k]=nums2[j]
            j+=1
        k+=1
    while i<len(nums1):
        arr[k]=nums1[i]
        i+=1
        k+=1
    while j<len(nums2):
        arr[k]=nums2[j]
        j+=1
        k+=1
    return arr
    
def median(nums1,nums2):
    arr=merge(nums1,nums2)
    print(arr)
    n=len(arr)
    median=-1
    if n%2!=0:
        median=arr[n//2]
    else:
        median=(arr[(n//2)-1]+arr[n//2])/2
    return median
print(median(nums1,nums2))

# Better
#tc= O(m+n) sc=O(1)
def better(nums1,nums2):
    count=0
    i=0
    j=0
    n1=len(nums1)
    n2=len(nums2)
    n=n1+n2
    #tracking variables
    idx1=(n1+n2)//2
    idx2=idx1-1
    el1=-1
    el2=-1
    
    while i<n1 and j<n2:
        if nums1[i]<nums2[j]:
            if count==idx1:
                el1=nums1[i]

            if count==idx2:
                el2=nums1[i]
                
            i+=1
        else:
            if count==idx1:
                el1=nums2[j]

            if count==idx2:
                el2=nums2[j]
                
            j+=1           
        count+=1

    while i<n1:
        if count==idx1:
            el1=nums1[i]

        if count==idx2:
            el2=nums1[i]
            
        count+=1
        i+=1
    while j<n2:
        if count==idx1:
            el1=nums2[j]

        if count==idx2:
            el2=nums2[j]
             
        count+=1
        j+=1
    
    if n %  2 ==1:
        return el1
    else:
        return (el1+el2)/2

print(better(nums1,nums2))


#optimal  
#tc = O(log(min(n1​,n2​))) sc= O(1)     
def optimal(nums1,nums2):
    n1=len(nums1)
    n2=len(nums2)
    if n1>n2:
        return optimal(nums2,nums1)
    low=0
    high=n1
    n=n1+n2
    left=(n1+n2+1)//2
    
    while low<=high:
        mid1=(low+high)//2
        mid2=left-mid1
        # default min val
        l1=float('-inf')
        l2=float('-inf')
        
        # default max  val
        r1=float('inf')
        r2=float('inf')
        
        if mid1 < n1:
            r1=nums1[mid1]
        if mid2 < n2:
            r2=nums2[mid2]
            
        if (mid1 - 1) >=0:
            l1=nums1[mid1-1]
        if (mid2 - 1) >=0:
            l2=nums2[mid2-1]
        
        #conditions for BS
        if l1<=r2 and l2<=r1:
            if n % 2 == 1:
                return max(l1,l2)
            else:
                return (min(r1,r2)+max(l1,l2))/2
        elif l1>r2:
            high=mid1-1
        else:
            low=mid1+1
            
print(optimal(nums1,nums2))


# Brute Force Intuition
# Merge both sorted arrays into a single sorted array.
# Median is just the middle element(s) of the merged array.
# Simple, but wastes extra space.

# Better Intuition
# We don't need the entire merged array.
# While performing merge, keep track only of the median index(es).
# When we reach those positions, store the elements and compute the median.
# Saves space by avoiding the merged array.

# Optimal Intuition
# Median depends only on the elements around the middle, not on the full merged array.
# Partition both arrays such that the left half contains exactly (n1+n2+1)//2 elements.
# Use binary search on the smaller array to find the correct partition.
# A partition is valid when:
# l1 <= r2
# l2 <= r1
# Once valid:
# Odd length → median = largest element on the left side.
# Even length → median = average of largest left and smallest right.

# Binary Search Movement
# If l1 > r2, we took too many elements from nums1 → move left.
# Else (l2 > r1), we took too few elements from nums1 → move right.
# One-line Core Idea

# Instead of finding the median directly, binary search for the partition where all left-side elements are ≤ all right-side elements.