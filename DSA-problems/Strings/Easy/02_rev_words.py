'''Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.'''

s="     the sky    ise blue    "#16
s2="eulb esi yks"#7
def brute(s): 
    s2=s.split(" ")
    s1=s2[::-1]
    s=""
    for i in range(len(s1)):
        if s1[i]!="":
            s+=s1[i]
            s+=" "
    
    return s.strip()
print(brute(s))

def optimal(s):
    return " ".join(s.split()[::-1])
print(optimal(s))