class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        fromleft = [1] * n
        fromright = [1] * n  

        for i in range(1, n):
            fromleft[i] = fromleft[i - 1] * nums[i - 1]

        for i in reversed(range(n - 1)):
            fromright[i] = fromright[i + 1] * nums[i + 1]

        return [fromleft[i] * fromright[i] for i in range(n)]
