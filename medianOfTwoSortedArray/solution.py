class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        tag = 0
        if((m+n)%2==0):
            tag = 1
        left = int((m+n)/2)
        if(m==0 and n == 0):
            return None
        if(m==0):
            if(tag==0):
                return nums2[left]
            else:
                return float((nums2[left]+nums2[left-1]))/2
        if(n==0):
            if(tag==0):
                return nums1[left]
            else:
                return float((nums1[left] + nums1[left-1]))/2
        return self.findm(nums1,nums2,0,m-1,0,n-1,left)
    
    def findm(self,nums1,nums2,start1,end1,start2,end2,left):
        m = len(nums1)
        n = len(nums2)
        median1 = int(left/2)
        median2 = left - median1
        if(left == 1):
            median1 = 1
        median1 -=1
        median2 -=1
        if(median1 > end1 - start1 ):
            median1 = end1-start1 
            median2 = left - median2
        elif(median2 > end2 - start2 ):
            median2 = end2 - start2 
            median1 = left - median2
#        elif(median1 < end1-start1 + 1 and median2 < end2 - start2 + 1):
        print(start1,end1,median1,start2,end2,median2)
        if(nums1[median1+start1]>nums2[median2+start2]):
            left = left - (median2+1)
            start2 = start2+median2+1
            end1 =start1+ median1
        elif(nums1[median1+start1]<nums2[median2+start2]):
            left = left - (median1+1)
            start1 = start1 + median1 + 1
            end2 = start2 + median2
        elif(nums1[median1+start1]==nums2[median2+start2]):
            return nums1[median1]
            
        if(start1>end1):
            return nums2[start2+left]
        if(start2>end2):
            return nums1[start1+left]
        if(left==0):
            if(nums1[start1]>nums2[start2]):
                return nums2[start2]
            else:
                return nums1[start1]
        return self.findm(nums1,nums2,start1,end1,start2,end2,left)
        
s = Solution()
print s.findMedianSortedArrays([1,3],[3,4])