class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0]) 
        low = 0
        high = (m )*(n ) - 1
        while low<=high:
            mid = (low+high)//2
            r , c = mid//n , mid%n
            print(r,c,mid,m,n)
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False          


        
