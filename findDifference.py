class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        answer1 =[]
        answer2 = []
        for i in set(nums1):
            if i not in set(nums2):
                answer1.append(i)
       
        for i in set(nums2):
            if i not in set(nums1):
                answer2.append(i)
        
        return[answer1 , answer2]

