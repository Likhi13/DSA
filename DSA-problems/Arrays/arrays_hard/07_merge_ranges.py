'''Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.'''

arr=[[1,3],[2,6],[8,10],[15,18]]
def brute(nums):
    arr=sorted(nums)
    print(arr)
    ans=[]
    for i in range(len(arr)):
        start=arr[i][0]
        end=arr[i][1]
        if len(ans)!=0 and end<=ans[-1][1]:
            continue
        for j in range(i+1,len(nums)):
            if arr[j][0]<=end:
                end=max(arr[j][1],end)
            else:
                break
        ans.append([start,end])
    return ans

print(brute(arr))
            
def optimal(nums):
    arr=sorted(nums)
    ans=[]
    for i in range(len(arr)):
        if len(ans)!=0 and ans[-1][1]>=arr[i][0]:
            end=max(ans[-1][1],arr[i][1])
            ans[-1][1]=end
        else:
            ans.append(arr[i])
    return ans
# print(optimal(arr))

    # arr=sorted(nums)
    # ans=[]
    # i=len(arr)-1
    # m=0
    # while i>m:
    #     first=arr[i][0]
    #     n=0
    #     j=i-1
    #     while j>=n:
    #         sec=arr[j][1]
            
    #         if first<=sec:
    #             ans.append([arr[j][0],arr[i][1]])

    #             j-=1
    #             i-=1
    #         else:
    #             sub=arr[i]
    #             if sub not in ans:
    #                 ans.append(sub)
    #         j-=1
    #     i-=1
             
    # return ans

    #     for i in range(len(arr)):
    #     set1=[]
    #     for j in range(arr[i][0],arr[i][1]+1):
    #         set1.append(j)
    #     for k in range(i+1,len(arr)):
    #         set2=[]
    #         for l in range(arr[k][0],arr[k][1]+1):
    #             set2.append(l)
    #         set3=set(set1).intersection(set(set2))
    #         if len(set3)!=0:
    #             set3=set(set1).union(set(set2))
    #             start=min(set3)
    #             end=max(set3)
    #             if [start,end] not in ans:
    #                 ans.append([start,end])
    #         else:
    #             if arr[i] not in ans:
    #                 ans.append([arr[i]])
    # return ans