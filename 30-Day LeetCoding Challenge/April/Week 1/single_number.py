# Time complexity O(n)
# without using extra memory
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        for i in unique_nums:
            count = nums.count(i)
            if count == 1:
                return i

# with extra memory
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        finder = {}
        for i in nums:
            if i not in finder:
                finder[i] = 1
            else:
                finder[i] += 1

        for k in finder:
            if finder[k] == 1:
                return k
