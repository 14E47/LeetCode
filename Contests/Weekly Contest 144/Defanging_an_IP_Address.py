class Solution:
    def defangIPaddr(self, address: str) -> str:
        r = ''
        for i in address:
            if i == '.':
                r += '[.]'
            else:
                r += i
        return r





address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
c = Solution().defangIPaddr(address)
print(c)