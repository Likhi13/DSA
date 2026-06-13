'''You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

 '''
bloomDay =[10,10]
m = 1
k = 1
def is_possible(arr,day,m,k):
    count=0
    boq=0
    for i in range(len(arr)):
        if arr[i]<=day:
            count+=1
        else:
            boq+=(count//k)
            count=0
    boq+=(count)//k
    if boq>=m:
        return True
    else:
        return False
            
    
def brute(bloomDay,m,k):
    for i in range(min(bloomDay),max(bloomDay)+1):
        if is_possible(bloomDay,i,m,k):
            return i
    return -1

def optimal(bloomDay,m,k):
    low=min(bloomDay)
    high=max(bloomDay)
    if len(bloomDay)<m*k:
        return -1
    while low<=high:
        mid=(low+(high-low)//2)
        if is_possible(bloomDay,mid,m,k):

            high=mid-1
        else:
            low=mid+1
    return low
print(optimal(bloomDay,m,k))
            
    
                