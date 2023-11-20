class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ans = 0
        maxvow = 0
        vowel = 'aeiou'
        
        for i, c in enumerate(s):
            if c in vowel:
                maxvow += 1
            if i >= k and s[i - k] in vowel:
                maxvow -= 1
            ans = max(ans, maxvow)
        return ans
