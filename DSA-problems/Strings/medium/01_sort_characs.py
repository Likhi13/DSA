'''Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.'''
s = "Aabb"
# TC=o(n log n) sc=o(n)
def brute(s):
    s1=""
    hashmap={}
    for k,v in enumerate(s):
        if v not in hashmap:
            hashmap[v]=1
        else:
            hashmap[v]+=1
    print(hashmap)
    sort=sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
    print(sort)
    for tup in sort:
        count=tup[1]
        i=0
        while i<count:
            s1+=tup[0]
            i+=1
    return s1 
# print(brute(s))

# intuition grouping characters by frequency
# mul string by int is possible ex:- ('b'*2)
def optimal(s):
    result=[]
    hashmap={}
    for k,v in enumerate(s):
        if v not in hashmap:
            hashmap[v]=1
        else:
            hashmap[v]+=1

    buckets=[[] for _ in range(len(s)+1)]
    print(buckets)
    for ch, count in hashmap.items():
        buckets[count].append(ch)
    print(buckets)

    for i in range(len(s),0,-1):
        for ch in buckets[i]:
            result.append(ch*i)
    return "".join(result)
      
print(optimal(s))

#using freq array for lowercase     
def optimal2(s):
    s1=""
    freq_arr=[(0,chr(i+ord('a'))) for i in range(26)]
    
    for ch in s:
        ind=ord(ch)-ord('a')
        freq_arr[ind]=(freq_arr[ind][0]+1, ch)
    
    freq_arr.sort(key=lambda x:(-x[0],x[1]))
    
    for i in range(len(freq_arr)):
        s1+=freq_arr[i][1]*freq_arr[i][0]
    return s1
        
    
    