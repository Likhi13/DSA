nums=[0,2,3,0,5,0,4]
#----------------Move zeroes to ENd--O(n^2)  because of pop(n)--------------
def moveZeros(nums):
    n=len(nums)-1
    while n>=0:
        if nums[n]==0:
            nums.pop(n)
            nums.append(0)
        n=n-1
    return nums

# print(moveZeros(nums))
#----------------OPTIMAL 2 pointer solution----O(n)--------
def moveZeros2(nums):
    lastNonZeroFoundAt=0 #lastnonzerofoundat==present position of 0 so we switch curr non zero num w "0" 
    
    for cur in range(len(nums)):
        if nums[cur]!=0:
            nums[cur],nums[lastNonZeroFoundAt]=nums[lastNonZeroFoundAt],nums[cur]
            lastNonZeroFoundAt+=1 
    return nums
# print(moveZeros2(nums))
#NOTE: if you are trying to append or perform operation to the end of array then iterate from backwards then the operation performed won;t effect iteratio
#NOTE: but if youre trying to iterate forward and perform operation backwards, the elements SHIFT LEFT so it skips some positions
