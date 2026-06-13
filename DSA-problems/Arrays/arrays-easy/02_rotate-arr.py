import array as a

nums=a.array('i', [1,2,3,4,6])
#ROTATE ARRAY BY ONE TO LEFT---------------------------------------
def rotateLeft(nums):
    x=nums[0]
    for i in range(1,len(nums)):
        nums[i-1]=nums[i]
    nums[len(nums)-1]=x
    return nums
# print(rotateLeft(nums))


#ROTATE K STEPS TO LEFT--------------------------------------------
def rotateLeftK(nums,k):
    for i in range(k):
        x=nums.pop(0)
        nums.append(x)
    return nums
# print(rotateLeftK(nums,2))
# -----------------------rotate left->"+" rotate right->"-"-------------------------
def rotate_leftk1(nums,k):
    new=[]
    for i in range(len(nums)):
        ind=((i-k)%len(nums))
        print(ind)
        new.append(nums[ind])
    return new
        
print(rotate_leftk1(nums,5))

def rotateRightK(nums,k):
    for i in range(k):
        x=nums.pop()
        nums.insert(0,x)
    return nums
# print(rotateRightK(nums,4))
#----using recursion
def rotateLeftK2(nums,k):
    if k<0:
        return nums
    x=nums[0]
    for i in range(1,len(nums)):
        nums[i-1]=nums[i]
    nums[len(nums)-1]=x
    return rotateLeftK2(nums,k-1)
# print(rotateLeftK2(nums,2))


#right rotate - from right to left-------------------------------------------
def rightRotate(nums,k):
    n=len(nums)
    k=k%n

    reverse(nums,0,n-1)
    reverse(nums,0,k-1)
    reverse(nums,k,n-1)
    return nums

def reverse(nums,left,right):
    if left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1

# print(rightRotate(nums,3))
