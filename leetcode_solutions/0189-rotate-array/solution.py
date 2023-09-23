class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a=[]
        k=k%len(nums)
        for i in range(len(nums)-k,len(nums)):
            a.append(nums[i])
        for i in range(0,len(nums)-k):
            a.append(nums[i])
        for i in range (len(nums)):
            nums[i]=a[i]


        
        
