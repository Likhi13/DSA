'''Given a non-empty grid mat consisting of only 0s and 1s, where all the rows are sorted in ascending order,
find the index of the row with the maximum number of ones.
If two rows have the same number of ones, consider the one with a smaller index. If no 1 exists in the matrix, return -1.'''

mat = [ [0,0,0], [0, 0, 0], [0, 0, 0] ]
# TC= O(n*m) SC=O(1)
def brute(mat):
    count_max=0
    idx=-1
    for i in range(len(mat)):
        count_row=0
        for j in range(len(mat[i])):
            count_row+=mat[i][j]
        if count_row > count_max:
            count_max=count_row
            idx=i
    return idx

print(brute(mat))

def lower_bound(arr,x):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=x:
            high=mid-1
        else:
            low=mid+1
    return low
#TC= O(n)* O(log m) SC=O(1)
def optimal(mat):
    count_max=0
    idx=-1
    for i in range(len(mat)):
        count_row=len(mat[i])-lower_bound(mat[i],1)
        print(count_row)
        if count_row>count_max:
            count_max=count_row
            idx=i
    return idx
print(optimal(mat))