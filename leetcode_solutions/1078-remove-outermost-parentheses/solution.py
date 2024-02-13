class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        sum=0
        start=0
        retstr=""
        for i in range (len(s)):
            if s[i]=="(":
                sum+=1
            elif s[i]==")":
                sum-=1
            if sum==0:
                retstr+=s[start+1:i]
                start=i+1
        return retstr
