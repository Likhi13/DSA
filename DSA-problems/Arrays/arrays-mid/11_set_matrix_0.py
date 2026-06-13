'''Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.'''
from array import array as arr
import numpy as np
matrix = [[1,1,1],
          [1,0,1],
          [1,1,1]]
    
matrix1= [[0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]]
    
# initialization using array mod and numpy mod and list of lists in py
    # rows=len(matrix)
    # cols=len(matrix[0])
    # tracker= [arr('i',[1]*cols) for _ in range(rows)]
    # # or
    # # tracker=np.ones((rows,cols),dtype=int)
    # # or
    # # tracker = [[0 for _ in range(cols)] for _ in range(rows)]

# BRUTE FORCE-O(n^3) WHy?--worst case-O(mn(m+n))
# --SPACE-O(mn)
def set_matrix(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    tracker=np.ones((rows,cols),dtype=int)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            tracker[i][j]=matrix[i][j]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if tracker[i][j]==0:
                for k in range(len(matrix[i])):
                    matrix[i][k]=0
                for l in range(len(matrix)):
                    matrix[l][j]=0
                                   
    return matrix

# BETTER SOLN-O(M x N)--space-O(m)+O(n)
def better(matrix):
    row=len(matrix)
    col=len(matrix[0])
    rows=[0]*row
    cols=[0]*col
    for i in range(row):
        for j in range(col):
            if matrix[i][j]==0:
                rows[i]=1
                cols[j]=1
    for i in range(row):
        for j in range(col):
            if rows[i]==1 or cols[j]==1:
                matrix[i][j]=0
    return matrix

                

# OPTIMAL-O(MxN)--SPACE-O(1)
# intuition:Use the first row and column as a notepad to remember
# which rows and columns must be zeroed, then apply those decisions afterward
def optimal(matrix):
    row=len(matrix)
    col=len(matrix[0])
    col0=1
    for i in range(row):
        for j in range(col):
            if matrix[i][j]==0:
                # mark i-th row
                matrix[i][0]=0
                # mark j-th col
                if j!=0:
                    matrix[0][j]=0
                else:
                    col0=0


    for i in range(1,row):
        for j in range(1,col):
            if matrix[i][j]!=0:
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
                    
    # marking 0th row 
    if matrix[0][0]==0:
        for j in range(col):
            matrix[0][j]=0
    # marking 0th col
    if col0==0:
        for i in range(row):
            matrix[i][0]=0
    return matrix

# brute=set_matrix(matrix1)
# print(brute)
# for i in range(len(matrix1)):
#     for j in range(len(matrix1[i])):
#         print(matrix1[i][j], end=" ")
#     print()
    
# btr=better(matrix1)
# print(btr)
# for i in range(len(matrix1)):
#     for j in range(len(matrix1[i])):
#         print(matrix1[i][j], end=" ")
#     print()
op=optimal(matrix1)
print(op)
# for i in range(len(matrix1)):
#     for j in range(len(matrix1[i])):
#         print(matrix1[i][j], end=" ")
#     print()

#  can do this or that

    # # marking 1-x rows as 0 
    # for i in range(1,row):
    #     if matrix[i][0]==0:
    #         for j in range(1,col):
    #             matrix[i][j]=0
    # # marking 1-y cols  as 0
    # for j in range(1,col):
    #     if matrix[0][j]==0:
    #         for i in range(1,row):
    #             matrix[i][j]=0
                
    # Or combined marking in a single loop 
    # for i in range(1,row):
    #     for j in range(1,col):
    #         if matrix[i][j]!=0:
    #             if matrix[i][0]==0 or matrix[0][j]==0:
    #                 matrix[i][j]=0

# def set_matrix():
#     pass
# print("Enter rows")
# row=int(input())
# print("ENter col")
# col=int(input())

# for i in range(row):
#     for j in range(col):

# User input

# m,n =map(int,input("Enter row and col: ").split())
# matrix1=[]
# for i in range(m):
#     row=[]
#     for j in range(n):
#         print(f"enter [{i}][{j}]")
#         row.append(int(input()))
#     matrix1.append(row)
# print(matrix1)