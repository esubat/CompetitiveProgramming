class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        result = 0

        for num in count:
            complement = k - num
            if complement in count:
                operations = min(count[num], count[complement])
                result += operations

        return result // 2
