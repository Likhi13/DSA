'''Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.'''
s = "ab"
t = "aa"
# TC=O(N^2) --SC=O(N)
def brute(s,t):
    S=len(s)
    T=len(t)
    if S==0 and T==0:
        return True
    elif S==0 or T==0:
        return False
    elif S!=T:
        return False
    hashmap={}
    i,j=0,0
    while i<S:
        if s[i] not in hashmap:
            hashmap[s[i]]=t[j]
        elif hashmap[s[i]]!=t[j]:
                return False
        i+=1
        j+=1
    print(hashmap)
    for key in hashmap:
        for key2 in hashmap:
            if hashmap[key]==hashmap[key2] and key!=key2:
                return False
        
    return True
# print(brute(s,t))

def optimal(s,t):
    S=len(s)
    T=len(t)
    if S!=T:
        return False
    hashmap={}
    i,j=0,0
    while i<S:
        if s[i] not in hashmap:
            hashmap[s[i]]=t[j]
        elif hashmap[s[i]]!=t[j]:
                return False
        i+=1
        j+=1
    s,t=t,s
    i,j=0,0
    hashmap={}
    while i<S:
        if s[i] not in hashmap:
            hashmap[s[i]]=t[j]
        elif hashmap[s[i]]!=t[j]:
                return False
        i+=1
        j+=1
    return True
print(optimal(s,t))
        
# optial using ZIP
# zip() combines two sequences position by position.
# But it generates them one by one (not storing full list).
# instead of:
# for i in range(len(s)):
#                c1 = s[i]
#                c2 = t[i]
# we do: for c1,c2 in zip(s,t):

def op2(s,t):
    if len(s)!=len(t):
        return False
    hashmap_s_t={}
    hashmap_t_s={}
    
    for c1,c2 in zip(s,t):
           if c1 in hashmap_s_t and hashmap_s_t[c1] != c2:
               return False
           if c2 in hashmap_t_s and hashmap_t_s[c2]!=c1:
               return False
           hashmap_s_t[c1]=c2
           hashmap_t_s[c2]=c1
    return True
print(op2(s,t))

#REAL OPTIMAL
def isomorphicString( s, t):
    m1, m2 = [-1] * 256, [-1] * 256
    
    for i in range(len(s)):
        if m1[ord(s[i])] != m2[ord(t[i])]:
            return False
        
        m1[ord(s[i])] = i
        m2[ord(t[i])] = i
    
    return True