class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mxsum = None
        csum = None
        for i in nums:
            if csum is None:
                mxsum = i
                csum = i
            else:
                if csum + i > i:
                    csum += i
                else:
                    csum = i

            if mxsum < csum:
                mxsum = csum

        return mxsum