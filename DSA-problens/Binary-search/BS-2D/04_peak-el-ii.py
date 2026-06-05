'''A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.

Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].

You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.

 '''

mat=[[10,20,15],
     [21,30,14],
     [7,16,32]]

#TC= O(n*m)  SC=O(1)
def brute(mat):
    n=len(mat)
    m=len(mat[0])
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            top=mat[i-1][j]if i-1>=0 else -1
            bottom=mat[i+1][j] if i+1<n else -1
            left=mat[i][j-1]if j-1>=0 else -1
            right=mat[i][j+1]if j+1<m else-1
            
            if left<mat[i][j]>right and top<mat[i][j]>bottom:
                return [i,j]
print(brute(mat))

#TC= O(n log m) SC=O(1)
def find_max_el(mat,n,col):
    max_el=-1
    row=-1
    for i in range(n):
        if mat[i][col]>max_el:
            max_el=mat[i][col]
            row=i
    return row
    
def optimal(mat):
    n=len(mat)
    m=len(mat[0])
    low=0
    high=m-1
    
    while low<=high:
        mid=(low+high)//2
        row=find_max_el(mat,n,mid)
        left=mat[row][mid-1] if mid-1 >=0 else -1
        right=mat[row][mid+1] if mid+1<m else -1
        if left<mat[row][mid]>right:
            return [row,mid]
        elif mat[row][mid]<left:
            high=mid-1
        else:
            low=mid+1
    return(-1,-1)       
print(optimal(mat))