'''Given an array nums of size n,
which denotes the positions of stalls,
and an integer k, which denotes the number of aggressive cows,
assign stalls to k cows such that the minimum distance between any two cows is the maximum possible.
Find the maximum possible minimum distance.
min of 2 cows will be given for sure'''
stalls = [0, 3, 4, 7, 10, 9]
k = 4
def can_we_place(stalls,dist,k):
    sorted_stalls=sorted(stalls)
    cows=1
    last_cow=sorted_stalls[0]
    
    for s in sorted_stalls:
        if s-last_cow>=dist:
            cows+=1
            last_cow=s
    return cows>=k

# TC= o((max-min)*n)+ n log n
def brute(stalls,k):
    #range: 1-(max(stalls)-min(stalls))
    range_req=max(stalls)-min(stalls)+1
    
    for dist in range(1,range_req):
        if can_we_place(stalls,dist,k)==False:
            #prev dist when it was true(max possible dist)
            return dist-1
            
    return -1
print(brute(stalls,k))

# TC= [o(log(max-min))* o(n)] + n log n
def optimal(stalls,k):
    low=1
    high=max(stalls)-min(stalls)
    while low<=high:
        mid=low+(high-low)//2
        if can_we_place(stalls,mid,k):
            low=mid+1
        else:
            high=mid-1
    return high
