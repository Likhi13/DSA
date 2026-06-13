'''Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.'''

s=" -+0 41 2c     "
def brute(s):
    INT32_MIN = -2**31
    INT32_MAX = 2**31 - 1
    s1=s.strip()# only strips starting and ending spaces not in middle
    # print(s1)
    ans=""
    for i in range(len(s1)):
        if s1[0]=='-' and i==0:
            ans+='-'
        elif s1[0]=='+' and i==0:
            continue
        elif not s1[i].isdigit():
            break
        else:
            ans+=s1[i]
    
    if ans=='' or ans=='-':
        ans=0
    num=int(ans)
    if num<INT32_MIN:
        num=INT32_MIN
    elif num>INT32_MAX:
        num=INT32_MAX
    return num           
print(brute(s))

#USING RECURSION
def helper(s,i,sign,num):
    max_int=2**31-1
    min_int=-2**31
    if i>=len(s) or not s[i].isdigit():
        return sign*num
    
    num=num*10+ int(s[i])
    if sign*num>max_int:
        return max_int
    if sign*num<min_int:
        return min_int
    
    return helper(s,i,sign,num)    
    

def atoi(s):
    i=0
    while i<len(s) and s[i]==' ':
        i+=1
    
    sign=1
    if i<len(s) and (s[i]=="+" or s[i]=="-"):
        if s[i]=="+":
            sign=1
        else:
            sign=-1
        i+=1
    num=0
    return helper(s,i,sign,num)
print(atoi(s))