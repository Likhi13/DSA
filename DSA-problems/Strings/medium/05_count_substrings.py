'''Count Number of Substrings:
You are given a string s and a positive integer k.
Return the number of substrings that contain exactly k distinct characters.'''
s = "pqpqs"
k = 2 
def brute(s,k):
    if len(s)==0:
        return 0
    distinct=0
    for i in range(len(s)):
        s1=""
        for j in range(i,len(s)):
            s1+=s[j]
            hashmap={}
            count=0
            for l in range(len(s1)):
                if s1[l] not in hashmap:
                    hashmap[s1[l]]=1
                    count+=1
            if count==k:
                distinct+=1
                              
    return distinct 
# print(brute(s,k))

def better(s,k):
    if len(s)==0:
        return 0
    distinct=0
    for i in range(len(s)):
        s1=""
        hashmap={}
        count=0
        for j in range(i,len(s)):
            s1+=s[j]
            if s[j] not in hashmap:
                hashmap[s[j]]=1
                count+=1
            else:
                hashmap[s[j]]+=1
            if count==k:
                distinct+=1
            elif count>k:
                break                          
    return distinct 
# print(better(s,k))

# finds substrings having atmost k distict charcs  i.e >=k
# using 2-pointers and sliding window
def optimal_p1(s,k):
    left=0
    right=0
    char_freq={}  #stores charac and frequency
    distinct=0

    while right<len(s):
        if s[right] not in char_freq:
            char_freq[s[right]]=1

        else:
            char_freq[s[right]]+=1
        #to remove one charac from hashmap so that it contains k distinct characs again ..continues till any one charac is removed from hashmap
        while len(char_freq)>k:
            char_freq[s[left]]-=1
            if char_freq[s[left]]==0:
                del char_freq[s[left]]
            left+=1
        
        distinct+=(right-left+1) 
        right+=1
    return distinct
def optimal_p2(s,k):
    atmost_k=optimal_p1(s,k)
    # print(atmost_k)
    atmost_k_1=optimal_p1(s,k-1)
    # print(atmost_k_1)
    return atmost_k-atmost_k_1
print(optimal_p2(s,k))
        
        
    
