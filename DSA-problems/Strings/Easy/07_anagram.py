'''An anagram is a word or phrase created by rearranging the letters of another word or phrase, using all the original letters exactly once.
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
'''
s = "anagram"
t = "nagaram"
#   TC- O(N LOG N)--SC-O(N)
def brute(s,t):
    ss=sorted(s)
    tt=sorted(t)
    return ss==tt
print(brute(s,t))
# Space complexity is O(n) in worst case, but O(1) if character set is fixed., TC=o(n)
def optimal(s,t):
    if len(s)!=len(t):
        return False
    hash1={}
    hash2={}
    for k,v in enumerate(s):
        if v not in hash1:
            hash1[v]=1
        else:
            hash1[v]+=1
    for k,v in enumerate(t):
        if v not in hash2:
            hash2[v]=1
        else:
            hash2[v]+=1
    return hash1==hash2
print(optimal(s,t))
    