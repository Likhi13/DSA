'''You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.'''
s="8"
def brute(s):
    s1=""
    max_odd=float('-inf')
    for i in range(len(s)):
        s1=s[i]
        if int(s1)%2!=0:
            max_odd=max(max_odd,int(s1))
        for j in range(i+1,len(s)):
            s1=str(s1)+s[j]
            num=int(s1)
            if num%2!=0:
                max_odd=max(max_odd,num)
    if max_odd!=float('-inf'):
        return max_odd
    else:
        return ""
# print(brute(s))

def better(s):
    if len(s)==0:
        return ""
    max_odd=float('-inf')
    s1=s[0]
    if int(s1)%2!=0:
        max_odd=int(s1)
    for i in range(1,len(s)):
        num=int(s1)
        if num%2!=0:
            max_odd=max(max_odd,num)
        s1=str(s1)+s[i]
        if int(s1)%2!=0:
            max_odd=max(max_odd,int(s1))
    if max_odd!=float('-inf'):
        return str(max_odd)
    else:
        return ""
print(better(s))

def optimal(s):
    if len(s)==0:
        return ""
    pos=-1
    for i in range(len(s)-1,-1,-1):
        if int(s[i])%2!=0:
            pos=i
            break
    if pos==-1:
        return ""
    s1=""
    for i in range(pos+1):
        s1+=s[i]     
    return s1
print(optimal(s))

            
                
