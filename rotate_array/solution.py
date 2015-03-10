class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        l = len(nums)
        r = []
        index=0
        if (k == 0):
            return nums
        for i in range(0,l,k):
            index+=1
            if(i+k>=l):
                break
            for j in range(i+k-1,i-1,-1):
                r.append(nums[j])
        for i in range(index,l):
            r.append(nums[i])
        return r

s = Solution()
print s.rotate([1],0)