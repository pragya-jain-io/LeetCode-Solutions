class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        max=0
        term=0
        for i in s:
            if i=="(":
                term+=1
            if i==")":
                term-=1
            if term>max:
                max=term
        return max

