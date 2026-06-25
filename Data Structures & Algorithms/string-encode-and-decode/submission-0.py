class Solution:

    def encode(self, strs: List[str]) -> str:
        final=""
        for s in strs:
            final+=s+"."
        return final

    def decode(self, s: str) -> List[str]:
        strs=s.split(".")
        strs.pop(len(strs)-1)
        return strs