# Given a 32-bit signed integer, reverse digits of an integer.

class Solution:
    def reverse(self, x: int) -> int:
        signed_range = [2147483647, -2147483647]
        if x >= 0:
            res = int(str(x)[::-1])
            if res <= signed_range[0]:
                return res
            else:
                return 0
        elif x < 0:
            res = int('-' + str(abs(x))[::-1])
            if res >= signed_range[1]:
                return res
            else:
                return 0
