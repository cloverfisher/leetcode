
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        lenc = len(candidates)
        result = []
        for i in range(lenc-1,-1,-1):
            k = candidates[i]
            if(k>target):
                continue
            elif(k==target):
                result.append([k])
 #               print "result~",result
            elif(k<target):
                
                newtarget = target - k
                newcandidates = candidates[0:i+1]
   #             print k , newtarget ,newcandidates
                a = self.combinationSum(newcandidates,newtarget)
 #               print a
                if len(a)> 0 :
                    for j in a:
                        j.append(k)
                        j.sort()
  #                      print j
                        result.append(j)
#        print "result",result,"candidate target", candidates, target
        return result

s = Solution()
print s.combinationSum([8,7,4,3], 11)