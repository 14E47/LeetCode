class Solution:
    def isArmstrong(self, N: int) -> bool:
        num = N
        digits = len(str(N))
        res = 0

        while num != 0:
            digit = num % 10
            res += pow(digit, digits)
            num //= 10

        if res == N:
            return True
        return False


