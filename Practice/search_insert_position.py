class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        if len(nums) == 0:
            return 0
        else:
            k = 0
            for i,v in enumerate(nums):
                if v == target:
                    return i
                elif v < target:
                    k = i+1
            return k

        # approach 1

        # if target in nums:
        #     return nums.index(target)
        # else:
        #     return len([i for i in nums if i<target])

        # approach 2

        # try:
        #     return nums.index(target)
        # except:
        #
        #     return len([i for i in nums if i<target])


A = [1,3,5,6]
B = 5

A = [1,3,5,6]
B = 2
# #
A = [3]
B = 4

A = [1,3,5,6]
B = 0

print(Solution().searchInsert(A, B))