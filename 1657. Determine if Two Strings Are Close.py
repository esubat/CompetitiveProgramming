class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """

        if len(word1) != len(word2):
            return False

        char_count1 = {}
        char_count2 = {}

        for char1, char2 in zip(word1, word2):
            char_count1[char1] = char_count1.get(char1, 0) + 1
            char_count2[char2] = char_count2.get(char2, 0) + 1

        if set(char_count1.keys()) != set(char_count2.keys()):
            return False

        return sorted(char_count1.values()) == sorted(char_count2.values())
