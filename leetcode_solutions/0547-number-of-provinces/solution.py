class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        def dfs(node,visited):
            print(visited)
            visited.add(node)
            for i in range(n):
                if i not in visited and isConnected[node][i]==1:
                    dfs(i,visited)
        n=len(isConnected)
        visited=set()
        count=0
        for i in range(n):
            if i not in visited:
                count+=1
                dfs(i,visited)
        return count

            
