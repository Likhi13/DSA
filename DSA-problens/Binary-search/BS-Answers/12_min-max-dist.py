'''Given a sorted array arr of size n, containing integer positions of n gas stations on the X-axis, and an integer k, place k new gas stations on the X-axis.
The new gas stations can be placed anywhere on the non-negative side of the X-axis, including non-integer positions.
Let dist be the maximum distance between adjacent gas stations after adding the k new gas stations.
Find the minimum value of dist.
Your answer will be accepted if it is within 1e-6 of the true value.'''
#intutions  listed below

import math
import heapq
arr = [1,13,17,23]
k = 5

#Brute TC=O(k * n), SC=O(n)
def brute(arr,k):
    n=len(arr)
    how_many=[0]*(n-1)
    for i in range(k):
        max_sec_len=-1
        max_ind=-1
        for j in range(n-1):
            sec_len=(arr[j+1]-arr[j])/(how_many[j]+1)
            if max_sec_len<sec_len:
                max_sec_len=sec_len
                max_ind=j
        how_many[max_ind]+=1
    
    max_dist=-1
    for i in range(n-1):
        sec_len=(arr[i+1]-arr[i])/(how_many[i]+1)
        max_dist=max(sec_len,max_dist)
    return max_dist

print(brute(arr,k))

#Better using max heap, TC= O(n + k log n) SC=O(n)
#pythons heap is min heap, so to use max heap we negate the values and store

def better(arr,k):
    n=len(arr)
    pq=[]
    how_many=[0]*(n-1)
    for i in range(n-1):
        sec_len=arr[i+1]-arr[i]
        heapq.heappush(pq,(-sec_len,i))
        
    for i in range(k):
        #find max Value o(1)
        _,sec_ind=heapq.heappop(pq)
        #increment stations in the section
        how_many[sec_ind]+=1
        new_sec_len=(arr[sec_ind + 1]-arr[sec_ind])/(how_many[sec_ind]+1)
        #takes log n time complexity
        heapq.heappush(pq,(-new_sec_len,sec_ind))
    max_dist,_=heapq.heappop(pq)
    return abs(max_dist)
print(better(arr,k))

#Optimal TC=O(n)+[O log(range)*O(n)] SC=O(1) using Binary search
def count_gas_stations(arr,dist): 
    count=0
    for i in range(len(arr)-1):
        num_in_bwn=math.ceil((arr[i+1]-arr[i])/dist)-1
    
        count+=num_in_bwn
    return count

def optimal(arr,k):
    low=0
    high=0
    for i in range(len(arr)-1):
        high=max(arr[i+1]-arr[i],high)
    diff=10**-6
    while (high-low>diff):
        mid=low+(high-low)/2
        gas_stations=count_gas_stations(arr,mid)
        if gas_stations>k:
            low=mid
        else:
            high=mid
    return high

print(optimal(arr,k))


# brute force
# Intuition:
# Every time, place the next gas station in the gap that currently has the largest section length.
# To find that gap, scan all gaps.
# Repeat this process k times.

# Better-max heap
# Intuition
# Brute force wastes time scanning all gaps every iteration.
# Store the current largest section of each gap in a max heap.
# The heap instantly tells us which gap should receive the next gas station.
# After splitting a gap, update only that gap in the heap.

# Optimal-Binary Search
# Intuition:
# Instead of deciding where to place stations, guess the final answer dist.
# Check: "Can I make every adjacent distance ≤ dist using at most k new stations?"
# If more than k stations are needed, dist is too small.
# Otherwise, dist is feasible, so try a smaller value.