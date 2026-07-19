class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s=[0]*26
        compare=[0]*26
        l=0
        for j in range(0,len(s1)):
            s[ord(s1[j])-ord('a')]+=1
        while l<len(s2):
            index=ord(s2[l])-ord('a')
            if s[index]>0:
                r=l+1
                compare[index]+=1
                while r-l<len(s1) and r<len(s2):
                    index=ord(s2[r])-ord('a')
                    compare[index]+=1
                    r+=1
                if compare==s:
                    return True
                else:
                    compare=[0]*26
            l+=1
        return False