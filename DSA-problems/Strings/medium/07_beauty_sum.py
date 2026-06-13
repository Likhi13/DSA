'''The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

For example, the beauty of "abaacc" is 3 - 1 = 2.
Given a string s, return the sum of beauty of all of its substrings.'''
import string
s = "aabcb"
#TC=O(N^3)--SC=O(N)
def brute(s):
    sum=0
    
    for i in range(len(s)):
        s1=''
        
        for j in range(i,len(s)):
            s1+=s[j]
            char_freq={}
            for k in range(len(s1)):
                if s1[k] not in char_freq:
                    char_freq[s1[k]]=1
                else:
                    char_freq[s1[k]]+=1
            high=max(char_freq.values())
            low=min(char_freq.values())
                
            sum+=(high-low)

    return sum
print(brute(s))

#TC=O(N^2)--SC=O(1)--(CONSTANT 26 CHARACS)
def optimal(s):
    sum=0
    for i in range(len(s)):
        char_freq={}
        char_freq = {ch: 0 for ch in string.ascii_lowercase}
        max_freq=0
        for j in range(i,len(s)):
            #min_freq has to be computed fresh as it, never reset properly for next substring 
            min_freq=float('inf')
            char_freq[s[j]]+=1
            max_freq=max(max_freq,char_freq[s[j]])
            #this makes constant 26 iterations and not 'n'-O(1)
            for v in char_freq.values():
                if v!=0:
                    min_freq=min(min_freq,v)   
            sum+=(max_freq-min_freq)


    return sum
print(optimal(s))