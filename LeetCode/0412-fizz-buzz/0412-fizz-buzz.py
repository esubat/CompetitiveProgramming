class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        d = {3: 'Fizz', 5: 'Buzz'}
        return [''.join([d[k] for k in d if i % k == 0]) or str(i) for i in range(1, n + 1)]      