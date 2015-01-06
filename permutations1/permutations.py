# it doesn't work . when I append u in line 26, the x will change. It is wield.
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        import pdb
        
        print "num",num
        b = []
        if len(num)<1:
            return b
        if len(num)==1:
            b.append(num)
       #     print b.append(num)
            return b
      #  num = list(range(5))
      #  num.remove(2)
      #  return num
        for u in num:
            print u
            print num
            num.remove(u)
            x = self.permute(num)
            pdb.set_trace()
            print 'x',x
            num.append(u)
            print "x",x
            for c in x:
                c.append(u)
            
        return list(set(x))

s = Solution()
alist = [1,2,3]
print s.permute(alist)