class Solution:
    def isValid(self, s: str) -> bool:
        current=""
        for i in range(0,len(s)):
            if s[i]=="(" or s[i]=="[" or s[i]=="{":
                current+=s[i]
            elif i>0:
                l=len(current)-1
                if s[i]==")" and current and current[-1]=="(":
                    current=current[:-1]
                elif s[i]=="]" and current and current[-1]=="[":
                    current=current[:-1]
                elif s[i]=="}" and current and current[-1]=="{":
                    current=current[:-1]
                else:
                    return False
            else:
                return False
        if current=="":
            return True
        else:
            return False