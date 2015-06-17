class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}

    def judge(self,s):
        l = len(s)
        if  s[l-1] != "*":
            return False
        else :
            while(l-1>0):
                l-=1
                if(s[l-1] != "*"):
                    break
            if l-1!=0:
                return self.judge(s[:l-1])
            else:
                return True

    def isMatch(self, s, p):
        l1= len(s)
        l2 = len(p)
        if(l1==0 and l2 ==0):
            return True
        if(l1 == 0 ):
            return self.judge(p)
        if(l2 == 0):
            return self.judge(s)
   #    print s,p
        temp1 = s[l1-1]
        temp2 = p[l2-1]
         #case1:not exist *
        if(temp1 != '*' and temp2 != '*'):
            if temp1 == temp2 or temp1 == '.' or temp2 == '.':
                if l1 == 1 and l2 ==1:
                    return True
                # elif (l1 ==1 and l2 >1):
                #     self.judge(p[:l2-1])
                #     or (l1 >1 and l2 ==1):
                #     return False
                return self.isMatch(s[:l1-1],p[:l2-1])
            else:
                return False
        else: #one of them exist '*'
            if temp1 == '*' and temp2 !='*':
                if(l1 == 1):
                    return False #s = '*' 
                while(l1 - 1 >=0):
                    l1-=1
                    if(s[l1]!='*'):
                        break
                if(s[l1]=='*'):
                    return False
                l1 +=1
                if s[l1-1] == p[l2-1] or s[l1-1] == '.' or p[l2-1] == '.':
                    if(l2==1 and l1 == 1):
                        return True
                    else:
                        return self.isMatch(s,p[:l2-1])or self.isMatch(s[:l1-1],p)
                else:
                    if(l1 == 1):
                        return False
                    else:
                        return self.isMatch(s[:l1-1],p)
            if temp1 != '*' and temp2 =='*':
                if(l2 == 1):
                    return False #s = '*' 
                while(l2 - 1 >=0):
                    l2-=1
                    if(p[l2]!='*'):
                        break
                if(p[l2]=='*'):
                    return False
                l2 +=1
                if s[l1-1] == p[l2-1] or s[l1-1] == '.' or p[l2-1] == '.':
                    if(l1==1 and l2 ==1):
                        return True
                    else:
                        return self.isMatch(s[:l1-1],p)or self.isMatch(s,p[:l2-1])
                else:
                    if(l2 == 1):
                        return False
                    else:
                        return self.isMatch(s,p[:l2-1])
            if temp1 == '*'and temp2 =='*':
                k1 = l1
                k2 = l2
                while(k1-1>=0):
                    k1-=1
                    if(s[k1]!='*'):
                        break
                while(k2-1>=0):
                    k2-=1
                    if(p[k2]!='*'):
                        break
                if (s[k1] == '*' and p[k2] == '*'):
                    return True
                elif s[k1] == '*':
                    return False
                elif p[k2] == '*':
                    return False
                if(k1==0 and k2 == 0):
                    return True
                if(k1+k2==1):
                    return False
                return self.isMatch(s[:k1],p) or self.isMatch(s,p[:k2])

            
solution = Solution()
# s = 'a'
# p = '.*..a*'
s = 'ab'
p = '.*..'
#print solution.judge("a*c***")
print solution.isMatch(s,p)