class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        elif x // 10 == 0:
            return True
        else:
            y = x
            num = ''
            while x != 0:
                num += str(x%10)
                x //= 10
            if y != int(num):
                return False
            return True


x = 8
c = Solution().isPalindrome(x)
print(c)
