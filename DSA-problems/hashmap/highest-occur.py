nums=[1,2,3,4,4,2,2,2,3,3,3]
def highest_occur(nums):
    hashmap={}
    for key,value in enumerate(nums):
        if value not in hashmap:
            hashmap[value]=1
        else:
            hashmap[value]+=1
    minf=float('inf')
    maxf=0
    minel=None
    maxel=None
    for key,value in hashmap.items():
        if value>maxf or(value==maxf and key<maxel):
            maxf=value
            maxel=key
        if value<minf or(value==minf and key<minel):
            minf=value
            minel=key
        return minel,maxel
    # max=0
    # min=None
    # for key,value in hashmap.items():
    #     if value>max:
    #         max=value
            
    #     if min==None:
    #         min=value
    #     elif value<min:
    #         min=value
    # # print(min)
    # # print(max)
    # for key,value in hashmap.items():
    #     if value==max:
    #         highkey=key
    #     if value==min:
    #         lowkey=key
    # return highkey,lowkey
            
print(highest_occur(nums))
        
        
        
        