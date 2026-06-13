'''Given an integer array nums of size n containing values from [1, n] and each value appears exactly once in the array,
except for A, which appears twice and B which is missing.
Return the values A and B, as an array of size 2,
where A appears in the 0-th index and B in the 1st index.
Note: You are not allowed to modify the original array.'''

nums = [3, 5,4,5, 1]
def brute(nums):
    hashmap={}
    arr=[]
    for i in range(len(nums)):
        if nums[i] not in hashmap:
            hashmap[nums[i]]=0
        if nums[i] in hashmap:
            hashmap[nums[i]]+=1
    print(hashmap)
    for n in hashmap:
        if hashmap[n]==2:
            arr.append(n)
            break
    
    n=len(nums)
    expected=n*(n+1)//2
    obtained=sum(nums)-arr[0]
    arr.append(abs(expected-obtained))
    return arr
print(brute(nums))

def optimal(nums):
    n=len(nums)
    ans=[]
    # B is missing num, A is repeating num
    expected_sum=n*(n+1)//2
    expected_sum_squares=n*(n+1)*((2*n)+1)//6
    
    obtained_sum=sum(nums)
    obtained_sum_squares=1
    for i in range(len(nums)):
        obtained_sum_squares+=nums[i]**2
    print(expected_sum,expected_sum_squares,obtained_sum,obtained_sum_squares)
    A=(((expected_sum_squares-obtained_sum_squares)//(expected_sum-obtained_sum))+(expected_sum-obtained_sum))//2
    B=A-(expected_sum-obtained_sum)
    ans.append(B)
    ans.append(A)   
    
    return ans
print(optimal(nums))