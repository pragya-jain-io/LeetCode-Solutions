class Solution(object):
    def generateParenthesis(self, n):
        """
        : type n : int
        : rtype : List[str]
        """
        
        def generate(s,open_count,close_count):
            if len(s)>=n*2:
                ans.append(s)
                return
            if open_count<n:
                generate(s+"(",open_count+1,close_count)
            if close_count<open_count:
                generate(s+")",open_count,close_count+1)
            
        ans=[]
        generate('',0,0)
        return ans

