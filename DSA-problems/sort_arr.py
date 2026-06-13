import array as a
nums=a.array('i', [-2, 2, 4, 4, 4, 4, 5, 5])

def is_sorted(nums):
    is_true=True
    for i in range(1,len(nums)):
        if nums[i-1]>nums[i]:
            is_true=False
    return is_true

# print(is_sorted(nums))

def unique1(nums):
    lis=[]
    for i in range(len(nums)):
        if nums[i] not in lis:
            lis.append(nums[i])
    to_arr=a.array('i',lis)
    return to_arr

def unique2(nums):
    n=len(nums)-1
    lis=[]
    i=0
    while n>=0:
        # print(n)
        lis.append(nums[i])
        print(nums[i])
        if nums[i] in lis:
            nums.remove(nums[i])
            n-=2
            print(n)
        i+=1
        
    return nums

def unique3(nums):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[j]==nums[i]:
                nums.remove(nums[i])
                nums.append(5000)
    return nums

# print(unique3(nums))
# print(unique1(nums))

def unique4(nums):
    if not nums:
        return 0
    k=1
    for i in range(1,len(nums)):
        if nums[i]!=nums[k-1]:
            nums[k]=nums[i]
            k+=1
    print(nums)
    return k
        

# print(unique4(nums)) 

def unique5(nums):
    n=len(nums)-1
    for i in range(n, 0, -1):  
        # print(i)
        if nums[i] == nums[i - 1]:
            nums.pop(i)
    return len(nums)

print(unique5(nums))

