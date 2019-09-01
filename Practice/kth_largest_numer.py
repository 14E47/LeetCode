class Solution:

    def findKthLargest(self,nums, k):

        def heapify(arr, n, i):
            l = 2 * i + 1
            r = 2 * i + 2
            largest = i

            if l < n and arr[largest] < arr[l]:
                largest = l

            if r < n and arr[r] > arr[largest]:
                largest = r

            if largest != i:
                arr[largest], arr[i] = arr[i], arr[largest]
                heapify(arr, n, largest)

        n = len(nums)
        for i in range(n,-1,-1):
            heapify(nums, n, i)
        print(nums)

        for j in range(k):
            print(nums)
            nums[0],nums[n-j-1] = nums[n-j-1],nums[0]
            print(nums)
            print('*'*19)
            heapify(nums,n-j-1,0)

        print(nums)

Solution().findKthLargest([1,2,3,4,5,6,7,8],4)