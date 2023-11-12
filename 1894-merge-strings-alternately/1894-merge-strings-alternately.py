class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        length_word1 = len(word1)
        length_word2 = len(word2)
        maxLength = max(length_word1, length_word2)
        result = ''

        for i in range(maxLength):
            if i < length_word1:
                result += word1[i]
            if i < length_word2:
                result += word2[i]

        return result