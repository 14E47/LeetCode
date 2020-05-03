class Solution:

    def __init__(self):
        self.memo = set()

    def isHappy(self, n: int) -> bool:

        num = 0

        while n != 0:
            d = n % 10
            num += d ** 2
            n //= 10

        if num == 1:
            return True

        if num in self.memo:
            return False

        self.memo.add(num)

        return self.isHappy(num)


