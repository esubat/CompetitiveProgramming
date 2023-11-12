class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        @esuba
        the lcm between two numbers a and b canbe found 
        LCM = a(a%b+1)
        in our case we need the smallest even multiple ,therefore the second number is 2
        thus LCM = n*(n%2 + 1)
        """

        return n*(n%2 + 1)