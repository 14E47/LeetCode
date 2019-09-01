class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:

        unique = set(A)
        sorted_set = sorted(list(unique), reverse=True)
        for i in sorted_set:
            if A.count(i) == 1:
                return i
        return -1