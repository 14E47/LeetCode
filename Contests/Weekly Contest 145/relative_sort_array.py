class Solution:
    def relativeSortArray(self, arr1, arr2):
        not_in_a2 = sorted([i for i in arr1 if i not in arr2])
        result = []

        for i in arr2:
            count = arr1.count(i)
            result += [i]*count
        result += not_in_a2

        return result


# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]

a1 = [2,3,1,3,2,4,6,7,9,2,19]
a2 = [2,1,4,3,9,6]

c = Solution().relativeSortArray(a1,a2)
print(c)