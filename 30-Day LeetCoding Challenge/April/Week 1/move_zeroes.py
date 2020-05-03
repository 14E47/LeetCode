class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = 0
        for i, v in enumerate(nums):
            if v != 0:
                if c != i:
                    nums[c] = v
                    nums[i] = 0
                c += 1


nums = [0, 0, 1]
nums = [0, 1, 0, 3, 12]
nums = [2, 1]
Solution().moveZeroes(nums)

