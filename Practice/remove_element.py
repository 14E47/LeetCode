class Solution:
    def removeElement(self, nums, val):
        i = 0
        while i != len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
        return nums


A = [3,2,2,3]
B = 3
print(Solution().removeElement(A, B))