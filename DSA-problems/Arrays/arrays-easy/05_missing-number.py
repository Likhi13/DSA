import array as a

nums=a.array('i', [1,2,3,4,6])
#-----------------------------------O(n)----Space for set-O(n)------
def missed3(nums):
    set_nums=set(nums)
    num=0
    while num in set_nums:
        num+=1
    return num
# print(missed3(nums))
#============OPTIMAL===O(1)==========
def missed4(nums):
    n=max(nums)
    actual_sum=n*(n+1)//2
    expected_sum=0
    for i in nums:
        expected_sum+=i
    return actual_sum-expected_sum
# print(missed4(nums))
    