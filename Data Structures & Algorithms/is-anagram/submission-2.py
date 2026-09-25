class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        if len(s)==0:
            return True
        thisDict1=dict()
        thisDict2=dict()
        for c in s:
            thisDict1[c]=thisDict1.get(c, 0)+1
        for c in t:
            thisDict2[c]=thisDict2.get(c, 0)+1
            
        if thisDict1==thisDict2:
            return True
        return False