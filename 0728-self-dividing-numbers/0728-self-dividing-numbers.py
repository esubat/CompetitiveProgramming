class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        self_deviding_nums =[]

        def is_self_deviding(num):
            for i in str(num):
                if str(i) == '0' or num%int(i) !=0:
                    return False
            return True
       
        for i in range(left,right+1):
            if is_self_deviding(i):
                self_deviding_nums.append(i)
        
        return self_deviding_nums

