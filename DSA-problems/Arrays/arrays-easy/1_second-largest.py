import array as a

nums=a.array('i', [1,2,3,4,6])
#SECOND LARGEST ELEMENT----------------------------------------------
def sl(nums):
    set_num=set(nums)
    snums=sorted(set_num)
    return snums[-2]