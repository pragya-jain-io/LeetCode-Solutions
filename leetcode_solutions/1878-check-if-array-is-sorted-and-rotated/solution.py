class Solution:
    def check(self, nums: List[int]) -> bool:
        flag=0
        for i in range(len(nums)-1):
          if nums[i]>nums[i+1]:
            flag = flag + 1
          
        if flag>=2:
          return False 
        if flag == 0:
          return True
        if nums[0]<nums[(len(nums))-1]:
          return False
        return True
