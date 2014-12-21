class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        returnnum = 1.0
        if n == 0:
            return 1
        elif n > 0:
            for i in range(0,n):
                returnnum = returnnum *x
#            return x*self.pow(x,n-1)
        elif n < 0:
            for i in range(n,0):
                returnnum = returnnum/x
#            return 1/x*self.pow(x,n+1)
        return returnnum
        
s = Solution()
print s.pow(0.00001,2147483647)