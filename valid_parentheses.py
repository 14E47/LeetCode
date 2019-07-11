class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(":")", "[":"]", "{":"}"}
        stack = []

        for i in s:
            if i in brackets:
                stack.append(i)
            else:
                if len(stack)!= 0:
                    last = stack.pop(-1)
                    if brackets[last] != i:
                        return False
                else:
                    return False
        if len(stack)!=0:
            return False
        return True

s = "()"
s = "()[]{}"
s = "(]"
s = "([)]"
s = "]"
s = ""
c = Solution().isValid(s)
print(c)
