# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

nums=[7,1,5,3,6,4]
#brute force
def buysell(nums):
    max_profit=0
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            profit=nums[j]-nums[i]
            max_profit=max(max_profit,profit)
    return max_profit
# print(buysell(nums))


# using kadane's algo also returning position- most optimal-
# =-------------------O(n)---O(1)
# nums=[7,1,5,3,6,4]
def bs(nums):
    max_profit=0
    buy=nums[0]
    start=0
    fstart=start
    fend=0
    if len(nums)<2:
        return max_profit,fstart, fend
    for i in range(1,len(nums)):
        sell=nums[i]
        profit=sell-buy

        if profit > max_profit:
            max_profit=profit
            fstart=start
            fend=i
            
        if profit<0:
            buy=nums[i]
            start=i
    return max_profit, fstart, fend
# print(bs(nums))


# most optimal kadanes without returnning positions
def stocks(nums):
    max_profit=0
    buy=nums[0]
    if len(nums)<2:
        return max_profit
    for i in range(1,len(nums)):
        sell=nums[i]
        profit=sell-buy
        
        if profit < 0:
            buy=nums[i]
        if profit>max_profit:
            max_profit=profit
    return max_profit
print(stocks(nums))

#trial
# nums=[7,1,5,3,6,4]
def stocks2(nums):
    max_profit=0
    buy=nums[0]
    if len(nums)<2:
        return max_profit
    for i in range(1,len(nums)):
        sell=nums[i]
        profit=sell-buy
        
        if profit < 0:
            buy=nums[i]
        if profit>max_profit:
            max_profit=profit
    return max_profit