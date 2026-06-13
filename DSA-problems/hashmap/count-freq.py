
nums=[1,2,3,4,2,3,1,2,3,4]

def count_freq(nums):
    hashmapi={}
    for key, value in enumerate(nums):
        if value not in hashmapi:
            hashmapi[value]=1
        else:
            hashmapi[value]+=1
    listt=[]
    for key, value in hashmapi.items():
        listt.append([key,value])
    return listt
print(count_freq(nums))