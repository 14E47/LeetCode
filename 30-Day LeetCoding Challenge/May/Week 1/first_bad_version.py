# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        if n == 1:
            if isBadVersion(n):
                return 1

        while right != left + 1:
            mid = (left + right) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid

        if isBadVersion(left):
            return left
        else:
            return right
