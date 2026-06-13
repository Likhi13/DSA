'''For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.'''


s = "MCMXCIV"
def brute(s):
    hashmap = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
    }
    i=0
    num=0
    while i<len(s):
        if i<len(s)-1:
            if s[i]=='I' and (s[i+1]=='V' or s[i+1]=='X'):
                num+=(hashmap[s[i+1]]-hashmap['I'])
                i+=2
            elif s[i]=='X' and (s[i+1]=='L' or s[i+1]=='C'):
                num+=(hashmap[s[i+1]]-hashmap['X'])
                i+=2
            elif s[i]=='C' and (s[i+1]=='D' or s[i+1]=='M'):
                num+=(hashmap[s[i+1]]-hashmap['C'])
                i+=2
            else:
                num+=hashmap[s[i]]
                i+=1
        else:
            num+=hashmap[s[i]]
            i+=1
    return num
print(brute(s))
            
