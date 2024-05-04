class Solution:
    def solveNQueens(self, n) :        
        
        def valid(x,y,arr,n):
            # top-left-diagonal
            row=x
            col=y
            while row>=0 and col>=0:
                if arr[row][col]=="Q":
                    return False
                row-=1
                col-=1
                
            # bottom-left-diagonal
            row=x
            col=y
            while row<n and col>=0:
                if arr[row][col]=="Q":
                    return False
                row+=1
                col-=1
                
            # left-row
            row=x
            col=y
            while col>=0:
                if arr[row][col]=="Q":
                    return False
                col-=1
            return True
                
        def solve(col,arr=[["." for _ in range(n)] for _ in range(n)],res=[]):
            if col==n:
                res.append(["".join(arr[j]) for j in range(n)])
                return 
                
            
            for row in range(n):
                if valid(row,col,arr,n):
                    arr[row][col]="Q"
                    solve(col+1,arr,res)
                    arr[row][col]="."
            return res
        return solve(0)
