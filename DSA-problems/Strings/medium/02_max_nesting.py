'''Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.'''
s = "(1+(2*3)+((8)/4))+1"
def optimal(s):
    if len(s)==0:
        return 0
    count=0
    max_count=0
    for i in range(len(s)):
        if  s[i]=='(':
            count+=1
            max_count=max(count,max_count)
        if s[i]==')':
            count-=1
    return max_count
print(optimal(s))
            