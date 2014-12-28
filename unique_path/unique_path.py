class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        s = 1
        if n == 1:
            return 1
        for i in range(n-1):
            s= s*(m+n-2-i)/(i+1)
        return s