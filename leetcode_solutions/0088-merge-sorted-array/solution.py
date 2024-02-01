class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        l1=m-1
        l2=n-1
        ans=m+n-1
        while ans>-1:
            if l2>-1 and l1>-1 and nums1[l1]>=nums2[l2] :
                nums1[ans]=nums1[l1]
                l1-=1
                ans-=1
            elif l2>-1 :
                nums1[ans]=nums2[l2]
                l2-=1
                ans-=1
            else:
                return




