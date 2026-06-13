'''Given a string s and an integer k, return the total number of substrings of s where at least one character appears at least k times.'''
s="abacb"
k=2
# intuition:counting substrings that are not valid
#i.e couting substrings that dont have at least one charc appear 'k' times 
def optimal(s,k):
    n=len(s)
    right=0
    left=0
    count=0
    char_freq={}
    total=n*(n+1)//2
    print(total)
    #counting substrings that are not valid
    #i.e couting substrings that dont have at least one charc appear 'k' times 
    while right<len(s):
        if s[right] not in char_freq:
            char_freq[s[right]]=1
        else:
            char_freq[s[right]]+=1

        while char_freq[s[right]]>=k:
            char_freq[s[left]]-=1
            left+=1
        count+=(right-left+1)
        right+=1
    return total-count
print(optimal(s,k))