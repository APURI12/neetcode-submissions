class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s=dict()
        for i,j in enumerate(nums):
            dif=target-j
            if dif in s:
                return [s[dif],i]
            s[j]=i

