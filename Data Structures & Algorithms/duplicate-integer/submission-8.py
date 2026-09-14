class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s={}
        for i in nums:
            if i in s:
                return True
            else:
                s[i]=0
        return False