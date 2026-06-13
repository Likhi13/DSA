'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".'''
strs = ["flower","flow","flight"]
# TC=O(N X M), SC=O(1)
def optimal(strs):
    if len(strs)==0:
        return ""
    word=strs[0]
    op=""
    min_len=float('inf')
    for i in range(len(strs)):
        length=len(strs[i])
        if length<min_len:
            min_len=length
            word=strs[i]
    print(word)
    if len(word)==0:
        return ""
    j=0
    loop=True
    while j<len(word) and loop:
        count=0
        for i in range(len(strs)):
            if word[j]==strs[i][j]:
                count+=1
            else:
                loop=False
                break
        if count==len(strs):
            op+=word[j]
        j+=1
    return op

print(optimal(strs))
# TC=o(n*log m + m) sc=0(m) , m=len 0f smallest word

                    