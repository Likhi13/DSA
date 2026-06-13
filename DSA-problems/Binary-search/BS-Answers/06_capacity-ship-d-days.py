'''A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

'''
weights = [3,2,2,4,1,4]
days = 3
def days_required(weights,c):
    days=1
    sumLoad=0
    for w in weights:
        if (sumLoad+w>c):
            days+=1
            sumLoad=w
        else:
            sumLoad+=w
    return days

def brute(weights,days):
    total=sum(weights)
    calDays=0
    for c in range(max(weights),total+1):
        calDays=days_required(weights,c)
        if calDays<=days:
            return c
print(brute(weights,days))

def optimal(weights,days):
    low=max(weights)
    high=sum(weights)
    calDays=1
    while low<=high:
        mid=low+(high-low)//2
        calDays=days_required(weights,mid)
        if calDays<=days:
            high=mid-1
        else:
            low=mid+1
    return low
print(optimal(weights,days))
        
            