class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ans = -1
        low = 0
        high = len(nums) - 1
        while low<=high:
            mid = (low + high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                ans = mid
                high = mid - 1
            elif nums[mid] < target:
                ans = mid + 1
                low = mid + 1
        return ans
        
