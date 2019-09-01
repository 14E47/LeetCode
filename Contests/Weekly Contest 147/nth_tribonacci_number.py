class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0,1,1]
        if n < len(t):
            return t[n]

        for i in range(3,n+1):
            t.append(sum(t[i-3:i]))
        return t[n]

n = 7
print(Solution().tribonacci(n))