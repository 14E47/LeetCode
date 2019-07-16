class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1




haystack = "hello"
needle = "ll"

haystack = "aaaaa"
needle = "bba"

haystack = "a"
needle = "a"

print(Solution().strStr(haystack, needle))