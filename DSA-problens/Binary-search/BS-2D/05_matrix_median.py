'''Given a 2D array matrix that is row-wise sorted. The task is to find the median of the given matrix.'''
matrix=[ [1, 4, 9],
        [2, 5, 6],
        [3, 7, 8] ] 

#Tc= o(n*m)+ (n*m) log (n*m)
def brute(matrix):
    r=len(matrix)
    c=len(matrix[0])
    arr=[0]*(r*c)
    k=0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            arr[k]=(matrix[i][j])
            k+=1
    sorted_arr=sorted(arr)
    print(sorted_arr)
    n=len(arr)
    if n%2==1:
        median=sorted_arr[n//2]
    return median
# print(brute(matrix)) 

def upper_bound(arr,x):
    low=0
    high=len(arr)-1
    
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>x:
            high=mid-1
        else:
            low=mid+1
    return low

def count_occurrance(matrix,x):
    '''Number of elements in the matrix that are <= x'''
    n=len(matrix)
    count=0
    for i in range(n):
        count+=upper_bound(matrix[i],x)
    return count

#TC= O(n log m * log(max-min))
def optimal(matrix):
    n=len(matrix)
    m=len(matrix[0])
    low=float('inf')
    high=float('-inf')
    for i in range(n):
        if low>matrix[i][0]:
            low=matrix[i][0]
        if high<matrix[i][m-1]:
            high=matrix[i][m-1]
    req=(m*n)//2
    #binary search on (max-min)
    while (low<=high):
        mid=low+(high-low)//2
        
        count=count_occurrance(matrix,mid)
        if count<=req:
               low=mid+1
        else:
            high=mid-1
    return low 
            
            
print(optimal(matrix))
    