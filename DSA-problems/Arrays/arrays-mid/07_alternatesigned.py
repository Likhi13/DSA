'''
Given an integer array nums of even length consisting of an equal number of positive and negative integers.Return the answer array in such a way that the given conditions are met:



Every consecutive pair of integers have opposite signs.


For all integers with the same sign, the order in which they were present in nums is preserved.


The rearranged array begins with a positive integer.
Input : nums = [2, 4, 5, -1, -3, -4]

Output : [2, -1, 4, -3, 5, -4]

Explanation:

The positive number 2, 4, 5 maintain their relative positions and -1, -3, -4 maintain their relative positions
'''
nums=[2, 4, 5, -1, -3, -4]
#Brute------O(N^2)
def altsigned(nums):
    pos=neg=0
    for i in range(0,len(nums),2):
        print(i)
        if nums[i]<0:
            for j in range(i,len(nums)):
                if nums[j]>0:
                    new=j
                    break
            nums[i],nums[new]=nums[new],nums[i]
        if nums[i+1]>0:
            for j in range(i,len(nums)):
                if nums[j]<0:
                    new=j
                    break
            nums[i+1],nums[new]=nums[new],nums[i+1]
    return nums
# print(altsigned(nums))
# nums=[3,1,-2,-5,2,-4]


#------Trying O(n)-O(1)--FAILED-NOT POSSIBLE--
#NOTE -WHY not possible?
'''
To preserve order:
You must shift elements, not swap
Shifting in arrays costs O(n)
Doing it repeatedly → O(n²)

So you either choose:
O(n²), O(1) space (your original idea)
O(n), O(n) space (this solution)
'''
#WRONG- breaks edge  cases
# def altsigned2(nums):
#     pos=neg=i=0
#     n=len(nums)
#     while i<n:
#         if nums[i]>0:
#             pos=i
#             break
#         i+=1
#     while i<n:
#         if nums[i]<0:
#             neg=i
#             break
#         i+=1
#     print(pos,neg)
#     # nums=[3,1,-2,-5,2,-4]
#     i=0
#     while i<n:
#         if nums[i]<0:
#             neg=i
#             nums[i],nums[pos]=nums[pos],nums[i]
#         if nums[i+1]>0:
#             pos=i+1
#             nums[i+1],nums[neg]=nums[neg],nums[i+1]
#         i+=2
#     return nums
# print(altsigned2(nums))

# BETTER -O(N)+O(N)--O(N)
#----------O(n)---O(n)-------
def altsigned3(nums):
    pos=[]
    neg=[]
    result=[]
    for i in range(len(nums)):
        if nums[i]>0:
            pos.append(nums[i])
        else:
            neg.append(nums[i])
    print(pos,neg)
    p=0
    n=0
    for i in range(0,len(nums)//2):
            result.append(pos[p])
            p+=1
            result.append(neg[n])
            n+=1
    #or
    # for i in range(len(pos)):
    #     result.append(pos[i])
    #     result.append(neg[i])
    return result
print(altsigned3(nums))


# OPTIMAL-O(N)--O(N)
def alt_sign_op(nums):
    med=[0]*len(nums)
    p=0
    n=1
    for i in range(len(nums)):
        if nums[i]>0:
            med[p]=nums[i]
            p+=2
        else:
            med[n]=nums[i]
            n+=2
    return med
        
# print(alt_sign_op(nums))

# when the nums are not equally pos or neg
def alt_signed_op_2(nums):
    pos=[]
    neg=[]
    med=[0]*len(nums)
    for i in range(len(nums)):
        if nums[i]>0:
            pos.append(nums[i])
        else:
            neg.append(nums[i])
    
    if len(pos)>len(neg):
        for i in range(len(neg)):
            med[2*i]=pos[i]
            med[2*i+1]=neg[i]
        p=len(neg)*2
        for i in range(len(neg),len(pos)):
            med[p]=pos[i]
            p+=1
    else:
        for i in range(len(pos)):
            med[2*i]=pos[i]
            med[2*i+1]=neg[i]
        n=len(pos)*2
        for i in range(len(pos),len(neg)):
            med[n]=neg[i]
            n+=1
    return med
print(alt_signed_op_2(nums))