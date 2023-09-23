class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=-1
        flag = 0
        for j in range(0,len(nums)):
            if nums[j]==0:
                i=j
                flag+=1
                break
        temp=i
        if flag==0:
            return 
        for j in range(temp+1,len(nums)):
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                if j-i>1:
                    i+=1
                else:
                    i=j
            
        



        
