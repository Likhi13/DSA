'''You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.'''
import numpy as np
matrix= [[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,16]]

# BRUTE_FORCE--TIME-O(n x n)--SPACE=O(n x n)
# 
def brute(matrix):
    n=len(matrix)
    dup=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dup[j][n-i-1]=matrix[i][j]
    return dup

# OPTIMAL- TIME-O(n x n)---SPACE-O(1)--INPLACE
def optimal(matrix):
    #first transpose matrix
    n=len(matrix)
    for i in range(n-1):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    
    # then reverse each row
    for i in range(n):
        for j in range(n//2):
            matrix[i][j],matrix[i][n-j-1]=matrix[i][n-j-1],matrix[i][j]
    
    # # rev each col instead of row for anti-clockwise
    # for i in range(n):
    #     for j in range(n//2):
    #         matrix[j][i],matrix[n-j-1][i]=matrix[n-j-1][i],matrix[j][i]
    return matrix

# br=brute(matrix)
# # print(brute(matrix))

# for i in range(len(matrix)):
#     for j in range(len(matrix)):
#         print(br[i][j],end=' ')
#     print()

op=optimal(matrix)
for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(op[i][j],end=' ')
    print()    
    