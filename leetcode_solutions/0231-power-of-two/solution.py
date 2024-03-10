class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n==0 or (n & n-1):
            return False
        else:
            return True
        
