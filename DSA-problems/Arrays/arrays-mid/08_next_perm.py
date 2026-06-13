'''A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.'''

nums=[3,2,1]
# BRUTE-FORCE--IN_PLACE-O(N^3)--O(1)
def next_perm1(n):
    for i in range(len(n)-1,0,-1):
        j=i-1
        
        if n[j]<n[i]:
            mink=float('inf')
            for k in range(j+1,len(n)):
                if n[j]<n[k]:
                    swap=n[k]
                    if swap<mink:
                        ind=k
            n[j],n[ind]=n[ind],n[j]
            for l in range(j+1,len(n)-1):
                for m in range(j+2,len(n)):
                    if n[l]>n[m]:
                        n[l],n[m]=n[m],n[l]
            return n
    i=0
    j=len(n)-1
    while i<j:
        n[i],n[j]=n[j],n[i]
        i+=1
        j-=1    
    return n
# print(next_perm1(nums))

# OPTIMIZED-O(1)--O(1)--Failed
# partly wrong- explained below
nums=[4,3,2,5,3,1]
def next_perm_op(n):
    j=-1
    for i in range(len(n)-1,0,-1):
        j_0=i-1
        if n[j_0]<n[i]:
            j=j_0
            break
    if j!=-1:
        mink=float('inf')
        for k in range(j+1,len(n)):
            if n[j]<n[k]:
                swap=n[k]
                if swap<mink:
                    mink=swap
                    ind=k
        n[j],n[ind]=n[ind],n[j]
        l=j+1
        m=len(n)-1
        while(l<m):
            n[l],n[m]=n[m],n[l]
            l+=1
            m-=1
        return n
    i=0
    j=len(n)-1
    while i<j:
        n[i],n[j]=n[j],n[i]
        i+=1
        j-=1    
    return n
# print(next_perm_op(nums))

# OPTIMIZED-O(1)--O(1)--WORKING
def next_perm_op1(nums):
    j=-1
    for i in range(len(nums)-1,0,-1):
        if nums[i-1]<nums[i]:
            j=i-1
            break
    if j==-1:
        l=0
        m=len(nums)-1
        while(l<m):
            nums[l],nums[m]=nums[m],nums[l]
            l+=1
            m-=1
    else:
        for i in range(len(nums)-1,j,-1):
            if nums[j]<nums[i]:
                nums[j],nums[i]=nums[i],nums[j]
                break
        l=j+1
        m=len(nums)-1
        while(l<m):
            nums[l],nums[m]=nums[m],nums[l]
            l+=1
            m-=1
    return nums

print(next_perm_op1(nums))
        
# You searched by value; this code searches by position,
# which works because the suffix is already sorted.
def optimal2(n) -> None:
    # 1. Find pivot
    j = -1
    for i in range(len(n) - 1, 0, -1):
        if n[i - 1] < n[i]:
            j = i - 1
            break

    # 2. If pivot exists, find rightmost successor
    if j != -1:
        for k in range(len(n) - 1, j, -1):
            if n[k] > n[j]:
                n[j], n[k] = n[k], n[j]
                break

    # 3. Reverse suffix
    l, r = j + 1, len(n) - 1
    while l < r:
        n[l], n[r] = n[r], n[l]
        l += 1
        r -= 1
    return n
# print(optimal2(nums))