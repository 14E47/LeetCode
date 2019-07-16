class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        strs.sort(key=len)
        prefix = ""
        word = strs[0]

        if len(strs)==0:
            return prefix
        elif len(strs)==1:
            return strs[0]

        for i,j in enumerate(word):
            for k in strs[1:]:
                if k[i] != j:
                    return prefix
            prefix += j
        return prefix






strs = ["flower","flow","flight"]
c = Solution().longestCommonPrefix(strs)
print(c)