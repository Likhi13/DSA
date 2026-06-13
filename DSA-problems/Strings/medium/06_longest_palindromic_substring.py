'''Given a string s, return the longest palindromic substring in s.'''
s="abababa"
#TC= O(N^2)--SC=O(N)
def optimal(s):
    if len(s)==0:
        return ""
    longest_palin=''
    for i in range(len(s)):
        #odd length substring
        left=i
        right=i
        while (left>=0 and right<len(s)) and( s[left]==s[right]):
            left-=1
            right+=1

        palin=s[left+1:right]
        if len(palin)>len(longest_palin):
            longest_palin=palin
    #even length substring
        left=i-1
        right=i
        #even if i=0 first check left>=0 so no problem
        while (left>=0 and right<len(s)) and( s[left]==s[right]):
            left-=1
            right+=1

        palin=s[left+1:right]
        if len(palin)>len(longest_palin):
            longest_palin=palin
    return longest_palin
print(optimal(s))    