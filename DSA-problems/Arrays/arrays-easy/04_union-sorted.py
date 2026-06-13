nums1=[1, 5, 7, 8, 8]
nums2 =  [3, 4, 6, 7, 9, 9]
#------------------Union of Sorted Arrays  Using Merge Sort-----------------
# this uses the merge step of merge sort but without the recursive divide phase, and with an added condition to skip duplicates.
#NOTE -not result → True
'''
Python stops

result[-1] != x ❌ NOT evaluated

✔ Safe
✔ Append happens

👉 This is the only time the second condition is skipped.
------------------------------------------------------
not result → False

Python MUST evaluate second condition

result[-1] != x → checked

✔ Duplicate check happens
✔ This is where the second condition is ESSENTIAL
'''

def union(nums1,nums2):
    arr=[]
    i=0
    j=0
    # not in py is ! 
    while i<len(nums1) and j<len(nums2):
        if nums1[i]==nums2[j]:
            # if !arr-> arr is empty meand false in boolean so if it is not empty ->true 
            if not arr or arr[-1]!=nums1[i]:# why this condition?- ans:(avoids adding duplicates) Only add x if it is different from the last added element
                arr.append(nums1[i])
            i+=1
            j+=1
        elif nums1[i]<nums2[j]:
            if not arr or arr[-1] != nums1[i]:
                arr.append(nums1[i])
            i+=1
        else:
            if not arr or arr[-1] != nums2[j]:
                arr.append(nums2[j])
            j+=1

        
    while i<len(nums1):
        if not arr or arr[-1]!=nums1[i]:
            arr.append(nums1[i])
        i+=1
        
    while j<len(nums2):
        if not arr or arr[-1]!=nums2[j]:
            arr.append(nums2[j])
        j+=1
        
    return arr
# print(union(nums1,nums2))
def union_sorted(nums1, nums2):
    arr = []
    i, j = 0, 0
    last = None  # track last appended to avoid duplicates

    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            if nums1[i] != last:
                arr.append(nums1[i])
                last = nums1[i]
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            if nums1[i] != last:
                arr.append(nums1[i])
                last = nums1[i]
            i += 1
        else:
            if nums2[j] != last:
                arr.append(nums2[j])
                last = nums2[j]
            j += 1

    while i < len(nums1):
        if nums1[i] != last:
            arr.append(nums1[i])
            last = nums1[i]
        i += 1

    while j < len(nums2):
        if nums2[j] != last:
            arr.append(nums2[j])
            last = nums2[j]
        j += 1

    return arr
#--------------------Unioin of sorted arrays-------------
def union2(nums1,nums2):
    union=set(nums1+nums2)
    to_list=list(union)
    
    sorted_union=sorted(to_list)
    return sorted_union
# print(union2(nums1,nums2))

#-------------Find Missing Number in Range n of size n array---O(n^2)------

def missed1(nums):
    num=0
    while num<=len(nums):
        if num in nums:
            num+=1
        else:
            return num

        
# print(missed1(nums))