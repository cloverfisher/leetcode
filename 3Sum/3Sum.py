class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    
    def threeSum(self, num):
        d= {}
        returnnum = []
        l = len(num)
        num.sort()
        if(len(num)<3):
            return returnnum
        for i in range(0,l):
            for j in range(i+1,l):
                temp = num[i]+num[j]
                if num[j]<=0 or num[i]>=0:
                    k = d.get(temp,[])
                    if [num[i],num[j]] not in k:
                        k.append([num[i],num[j]])
                    d[temp] = k
        #            print d
        negative = d.keys()
        for n in negative:
            if -n in num:
                for i in d[n]:
                    i.append(-n)
                    i.sort()
                    if i not in returnnum:
                        returnnum.append(i)
        zero = 0
        for i in num:
            if i == 0:
                zero+=1
        if(zero == 2):
            returnnum.remove([0,0,0])
        return returnnum

num = [0,0,-1,1,2,-1,-2,-3]
s = Solution()
print s.threeSum(num)