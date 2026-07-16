class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=len(s)
        if length==0:
            return 0
        current={s[0]:0}
        final=1
        start=0
        i = 1
        while i < length:
            if s[i] not in current:
                current[s[i]]=0
                i += 1
            else:
                if final<i-start:
                    final=i-start
                start = start + 1
                i = start
                current={}
                if i < length:
                    current[s[i]]=0
                    i += 1
        if final<length-start:
                final=length-start
        return final