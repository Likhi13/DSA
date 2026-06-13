# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

# Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

# Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.
s = "(())(()())"

def brute(s):
    start=0
    ind=[]
    ind.append(0)
    for i in range(len(s)):
        if s[i]=='(':
            start+=1
        else:
            start-=1
        if start==0:
            ind.append(i)
            if i+1 <len(s):    
                ind.append(i+1)
    s1=""
    for i in range(len(s)):
        if i in ind:
            continue
        else:
            s1+=s[i]
    return s1
# print(brute(s))
# s = "()(())"
def optimal(s):
    s1=""
    start=0

    for i in range(len(s)):
        if s[i]==')':
            start-=1
        if start!=0:
            s1+=s[i]
        if s[i]=='(':
            start+=1
    return s1
print(optimal(s))        

def optimal2(s):
    s1=""
    level=0
    for i in range(len(s)):
        if s[i]=='(':
            if level>=0:
                s1+=s[i]
            level+=1
        elif s[i]==")":
            
            if level>0:
                s1+=s[i]
            level-=1
                
            
               
                
            