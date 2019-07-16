

class Solution:
    def transpose(self, A):
        r = len(A)
        c = len(A[0])
        T = []

        for i in range(c):
            sub = []
            for j in range(r):
                sub.append(A[j][i])
            T.append(sub)

        return T


A = [[1,2,3],[4,5,6],[7,8,9]]
c = Solution().transpose(A)
print(c)
