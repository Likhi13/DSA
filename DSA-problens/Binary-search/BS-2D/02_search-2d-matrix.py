'''You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.'''
matrix = [[1,3,5,7],
          [10,11,16,20],
          [23,30,34,60]]
target = 3

def better(matrix,target):
    
    for i in range(len(matrix)):
        low=0
        high=len(matrix[i])-1
        while low<=high:
            mid=(low+high)//2
            if matrix[i][mid]==target:
                return True
            elif matrix[i][mid]<target:
                low=mid+1
            else:
                high=mid-1
    return False
print(better(matrix,target))

def optimal(matrix,target):
    lowr=0
    highr=len(matrix)-1
    while lowr<=highr:
        
        mid_r=(lowr+highr)//2
        if target<matrix[mid_r][0]:
            highr=mid_r-1
        elif target>matrix[mid_r][-1]:
            lowr=mid_r+1
        else:
            row=matrix[mid_r]
            lowc=0
            highc=len(matrix[mid_r])-1
            while lowc<=highc:
                mid_c=(lowc+highc)//2
                if row[mid_c]==target:
                    return True
                elif row[mid_c]<target:
                    lowc=mid_c+1
                else:
                    highc=mid_c-1
            return False
    return False
print(optimal(matrix,target))
            
        
        
            