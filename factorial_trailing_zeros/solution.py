class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        r = 0
        while(n>=5):
            n/=5
            r +=n
        return r