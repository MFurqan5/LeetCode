class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0 
        divisor = 1000
        while divisor <= n:
            total += n -divisor +1
            divisor *= 1000

        return total