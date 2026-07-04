'''Given a positive integer n, find the sum of all integers in the range [1, n] inclusive that are divisible by 3, 5, or 7.

Return an integer denoting the sum of all numbers in the given range satisfying the constraint.'''
n=7
def sum_multiples(n):
    sum=0
    for i in range(1,n+1):
        if i % 3 ==0 or i % 5==0 or i % 7==0:
            sum+=i
    return sum
print(sum_multiples(n))