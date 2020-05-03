class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = {}
        for j in J:
            jewels[j] = True

        count = 0
        for s in S:
            check = jewels.get(s)
            if check:
                count += 1
        return count

J = "aA"
S = "aAAbbbb"
print(Solution().numJewelsInStones(J, S))
