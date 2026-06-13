

name="abaabab"
hashmapc={}
for key,value in enumerate(name):
    if value not in hashmapc:
        hashmapc[value]=1
    else:
        hashmapc[value]+=1
print(hashmapc)