class Solution:
    def median(self,nums1,nums2):
        low = 0
        high = len(nums1)
        left = (len(nums1)+len(nums2)+1)/2
        while low<=high:
            mid1 = (low+high)//2
            mid2 = int(left - mid1)

            # l1, l2 = float("-inf"), float("-inf")
            # r1, r2 = float("inf"), float("inf")
            # if mid1 < len(nums1): 
            #     r1 = nums1[mid1-1]
            # if mid2 < len(nums2): 
            #     r2 = nums2[mid2-1]  
            # if mid1-1>=0:
            #     l1 = nums1[mid1-1]
            # if mid2-1>=0:
            #     l2 = nums2[mid2-1]
            
            # Get the left and right elements for both partitions
            l1 = float("-inf") if mid1 == 0 else nums1[mid1 - 1]
            r1 = float("inf") if mid1 == len(nums1) else nums1[mid1]
            
            l2 = float("-inf") if mid2 == 0 else nums2[mid2 - 1]
            r2 = float("inf") if mid2 == len(nums2) else nums2[mid2]
            
            if l1<=r2 and l2<=r1: 
                if (len(nums1)+len(nums2))%2==1:
                    return max(l1,l2)
                else:
                    return (max(l1,l2)+min(r1,r2))/2.0
            elif l1>r2:
                high = mid1-1
            else:
                low = mid1+1
        return 0
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            return self.median(nums2,nums1)
        else:
            return self.median(nums1,nums2)
        return 0
