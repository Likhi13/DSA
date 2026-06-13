'''Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.'''
from math import ceil
piles = [3,6,7,11]

h = 8

def brute(p,h):
    m=max(p)
    for i in range(1,m+1):
        total_hrs=0
        for j in range(len(piles)):
            # total hours to complete one pile= no.of bananas in pile / bananas eaten per hour
            total_hrs+=ceil(piles[j]/i)
        if total_hrs<=h:
            return i
print(brute(piles,h))

def optimal(p,h):
    m=max(p)
    low=1
    high=m
    while low<=high:
        mid=(low+(high-low)//2)
        total_hrs=0
        for j in range(len(p)):
            total_hrs+=ceil(p[j]/mid)
  
        if total_hrs<=h:
            high=mid-1
        else:
            low=mid+1
    return low
print(optimal(piles,h))
        
                   
            
                
                
        
            
            
            
            
        