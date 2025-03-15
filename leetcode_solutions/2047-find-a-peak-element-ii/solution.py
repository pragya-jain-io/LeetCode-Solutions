class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        def checkPeak(mat,i,j):
            if i>0:
                if mat[i-1][j]> mat[i][j]:
                    return [False,0]
            if i<len(mat)-1:
                if mat[i+1][j]> mat[i][j]:
                    return [False,1]
            return [True,-1]  

        low = 0
        high = len(mat)-1
        while low<=high:
            mid = (low+high)//2
            max_idx = mat[mid].index(max(mat[mid]))
            peak = checkPeak(mat,mid,max_idx)
            if peak[0]:
                return [mid,max_idx]
            else:
                if peak[1]==0:
                    high = mid-1
                else:
                    low = mid+1
            



