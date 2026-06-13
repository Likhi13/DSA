'''Given an m x n matrix, return all elements of the matrix in spiral order.

'''

nums=[[1,2,3,1,9],
      [4,5,6,2,8],
      [7,8,9,3,7],
      [4,5,6,7,6],
      [5,4,3,2,1]]
# ansr=[1,2,3,6,9,8,7,4,5]
# nums = [
#     [ 1,  2,  3],
#     [ 4,  5,  6],
#     [ 7,  8,  9],
#     [10, 11, 12]
# ]
nums1 = [
    [ 1,  2,  3,  4,  5],
    [ 16, 17, 18,19, 6],
    [15, 24, 25, 20, 7],
    [14, 23, 22, 21, 8],
    [13, 12, 11, 10, 9]
]

# IT  ONLY HAS ONE SOLN AND IT IS OPTIMAL
# INTUITION: “I traverse the matrix by maintaining shrinking boundaries
# and printing one outer layer at a time until nothing remains.”
# O(N x M)--O(N x M)
def optimal(nums):
    right=len(nums[0])-1
    bottom=len(nums)-1
    left=0
    top=0
    ans=[]
    while left<=right and top<=bottom:
        for i in range(left,right+1):
            ans.append(nums[top][i])
        top+=1
        for i in range(top,bottom+1):
            ans.append(nums[i][right])
        right-=1
        if top<=bottom:
            for i in range(right,left-1,-1):
                ans.append(nums[bottom][i])
            bottom-=1
        if left<=right:
            for i in range(bottom,top-1,-1):
                ans.append(nums[i][left])
            left+=1
    return ans
print(optimal(nums1))
    



















# taking input
# m,n =map(int,input("Enter row and col: ").split())

# matrix=[]
# for i in range(m):
#     print(f"Enter {i} row elements")
#     row=list(map(int,input().split()))
#     matrix.append(row)
# for r in matrix:
#     print(r)

# matrix1=[]
# for i in range(m):
#     row=[]
#     for j in range(n):
#         print(f"enter [{i}][{j}]")
#         row.append(int(input()))
#     matrix1.append(row)
# print(matrix1)
        
        