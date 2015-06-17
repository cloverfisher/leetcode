class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
    	l = len(nums)
    	result = []
    	a = nums.remove(1)
    	print a 
    	return result



s = Solution()
nums= [1,2,3,4,5,6,7]
k = 3
print(s.rotate(nums,k))