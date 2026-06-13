'''Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:'''
num=5
# HAS ONLY BRUTE=OPTIMAL
# tc- o(n^2)--sc-o(n^2) output -extra space-o(1)
# my solution
def optimal(num):
    arr=[]
    for i in range(num):
        sub=[1]
        if i>=1:
            prev=arr[i-1]
            for j in range(1,len(prev)):
                sum=prev[j-1]+prev[j]
                sub.append(sum)
            sub.append(1)
        arr.append(sub)
    return arr
print(optimal(num))

# another soln using formula nCr
def row_gen(row):
    ans=1
    temp=[]
    temp.append(ans)
    for col in range(1,row):
        ans*=(row-col)
        ans=ans//col
        temp.append(ans)
    return temp
def triangle(n):
    tri=[]
    for i in range(1,n+1):
        tri.append(row_gen(i))
    return tri
print(triangle(num))

        
        