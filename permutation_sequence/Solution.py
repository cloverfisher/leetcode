class Solution:
    # @return a string
    def getPermutation(self, n, k):
        numLength = []
        numleft = range(1,n+1)
    #    print numleft
        resultNum = []
        temp = 1
        for i in range(1,n):
            temp *= i
            numLength.append(temp)
        if n < 2 :
            return "1"
        for i in range(0,n-1):
            for t in range(n-i,-1,-1):
                if k > t * numLength[n-2-i]:
                    resultNum.append(numleft[t])
                    k = k - t * numLength[n-2-i]
                    numleft.remove(numleft[t])
                    break
        resultNum.append(numleft[0])
        hehe = ""
        for i in resultNum:
            hehe = hehe+str(i)
        return hehe

s = Solution()
print s.getPermutation(4,3)