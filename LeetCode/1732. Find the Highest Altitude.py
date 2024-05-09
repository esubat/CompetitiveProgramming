class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        res = 0
        height = 0
        for i in gain:
            height += i
            res = max(res,height)
        return res
