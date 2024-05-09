class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def modifier(s1, s2):
            while s1.startswith(s2):
                s1 = s1[len(s2):]
            return s1           
        if len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)
        if not str1.startswith(str2):
            return ''
        if not str2:
            return str1
        return self.gcdOfStrings(str2, modifier(str1, str2))
