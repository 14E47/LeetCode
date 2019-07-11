class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        romans = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        prev = 0
        for i in s[::-1]:
            if prev == 0:
                number += romans[i]
            elif romans[i] < prev:
                number -= romans[i]
            else:
                number += romans[i]
            prev = romans[i]

        return  number

s = 'XCIV'
s = 'III'
s = "IV"
s = "IX"
s = "LVIII"
s = "MCMXCIV"
c = Solution().romanToInt(s)
print(c)