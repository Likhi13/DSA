'''Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom'''

matrix = [[1, 4, 7, 11, 15],
          [2, 5, 8, 12, 19],
          [3, 6, 9, 16, 22],
          [10,13,14,17, 24],
          [18,21,23,26, 30]]

target = 45
#TC= O(m*n) SC=O(1)
def brute(matrix,target):
    for i  in range(len(matrix)):
        for j in range(len(matrix[i])):
            if target==matrix[i][j]:
                return True
    return False
print(brute(matrix,target))

#TC= O(m log n) SC=O(1)
def better(matrix,target):
    for i in range(len(matrix)):
        row=matrix[i]
        low=0
        high=len(row)-1
        while low<=high:
            mid=(low+high)//2
            if target==row[mid]:
                return True
            elif target>row[mid]:
                low=mid+1
            else:
                high=mid-1
    return False
#TC = O(m+n), SC= O(1)
def optimal(matrix,target):
    m=len(matrix)
    n=len(matrix[0])
    row=0
    col=n-1
    while row<m and col>=0:
        if target==matrix[row][col]:
            return True
        elif target<matrix[row][col]:
            col=col-1
        else:
            row=row+1
    return False
print(optimal(matrix,target))
        