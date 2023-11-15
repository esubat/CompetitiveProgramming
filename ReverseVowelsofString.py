class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = list(s)
        vowels = ["a","e","i","o","u"]
        left = 0
        right = len(s)-1
        while left < right:
            if s[left].lower() in vowels and s[right].lower() in vowels:
               chars[left] , chars[right] = chars[right] , chars[left]
               left+=1
               right -= 1

            elif s[left].lower() in vowels:
                right -= 1
            else:
                left +=1
        
        return "".join(chars)
