class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        start=n-1
        flag=0
        for i in range(n-1,-1,-1):
            if s[i]==" ":
                if flag==0:
                    s=s[:i]
                if flag==1:
                    break
            else:
                flag=1
                start=i
        if start==0:
            return s
        n = len(s)
        end = len(s)-1
        temps = start
        flag = 0
        for i in range(start-1,-1,-1):
            if s[i]==" ":
                if flag==0:
                    pass
                if flag==1:
                    flag=0
                    s=s+" "+s[start:end+1]

            else:
                if flag==0:
                    end=i
                flag=1
                start=i
        
        if flag==1:
            return s[temps:]+" "+s[start:end+1]
        return s[temps:]








                

        
