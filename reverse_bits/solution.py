class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        r=0 #r is reverse return integer
        for i in range(0,32):
            k=n%2
            r*=2
            r+=k
            n=n/2
        return r
        