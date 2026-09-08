class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        total =0
        if n>= 1000:
            total += n - 999

        if n >= 1000000:
            total += n - 999999

        if n >= 1000000000:
            total += n - 999999999

        return total