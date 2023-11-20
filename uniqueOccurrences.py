class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = {}
        for num in arr:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        occurrences = set()

        for value in count.values():
            if value in occurrences:
                return False
            occurrences.add(value)

        return True
