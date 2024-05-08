class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[-1,]*(n)
        def stairs(n):
            if n==0:
                return 1
            if n<0:
                return 0
            if dp[n-1]!=-1:
                return dp[n-1]
            else:
                dp[n-1] = stairs(n-1) + stairs(n-2)
                return dp[n-1]
        return stairs(n)
        
