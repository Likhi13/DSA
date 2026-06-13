import array as a

nums=a.array('i', [1,2,3,4,6])
#-----------Linear Search----------------------------

def LinearSearch(nums,target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i
        
    return -1
# print(LinearSearch(nums,3))