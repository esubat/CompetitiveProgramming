class Solution(object):
    def searchRange(self, nums, target):

        #check if the input list is empty , if so return [-1,-1]
        if not nums:
            return [-1 , -1]

        left = 0
        right = len(nums) - 1
        output = [-1,-1]
        
        while left < right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle

        if nums[left] != target:
            return output

        output[0] = left
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2 + 1
            if nums[middle] <= target:
                left = middle
            else:
                right = middle - 1

        output[1] = right
        return output