class Solution:
	def numTrees(self, n):
		returnnum = 0;
		if (n == 1) :
			return 1
		elif (n ==0):
			return 1
		else:
			for i in range(1,n+1):
				returnnum += self.numTrees(i-1) * self.numTrees(n-i)
			return returnnum

s = Solution()
print s.numTrees(3)
