class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        temp = s.split()
        size = len(temp)
        l = []
        for i in xrange(size):
            l.append(temp[size-i-1])
            
        a = ' '.join(l)
        return a
