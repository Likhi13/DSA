import array as a

nums=a.array('i', [1,2,3,4,6])
#------------------------Max Consec Ones---------------O(n)------------
def consec1s(nums):
    count=0
    max_count=0
    for i in range(len(nums)):
        if nums[i]==1:
            count+=1
        else:
            max_count=max(count,max_count)
            count=0
    max_count=max(count,max_count)#if at the end there are max ones then it does't enter else condition as there is no 0 after 1s, so we have to check again after the loop
    return max_count
# print(consec1s(nums))