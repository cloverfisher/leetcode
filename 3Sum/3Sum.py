class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    
    def threeSum(self, num):
        negativenum = {}
        positivenum = {}
        negativenum2 = {}
        positivenum2 = {}
        returnnum = []
        if(len(num)<3):
        	return returnnum
        for i in num:
        	if(i<0):	#negetivenum
        		if(negativenum.has_key(i)):
        			negativenum2[i]=negativenum2.setdefault(i,0)+1
        		negativenum[i]=1
        	else:
        		if(positivenum.has_key(i)):
        			positivenum2[i]=positivenum2.setdefault(i,0)+1
        		positivenum[i] = 1
        self.twoAddOne(negativenum2,positivenum,returnnum)
        self.twoAddOne(positivenum2,negativenum,returnnum)
        self.oneAddOne(negativenum,positivenum,returnnum)
        self.oneAddOne(positivenum,negativenum,returnnum)
        if(positivenum.has_key(0)):
	        if(positivenum2[0]>1):
	        	returnnum.append([0,0,0])
        return returnnum

    def twoAddOne(self,num2,num1,lists):
    	for i in num1:
    		if(num2.has_key(-i)):
    			lists.append([i,i,-2*i])

    def oneAddOne(self,num1,num2,lists):
    	size1 = len(num1)
    	size2 = len(num2)
    	num = num1.keys()
    	for i in range(size1):
    		for j in range(i+1,size1):
    			if(num2.has_key(-num[i]-num[j])):
    				lists.append([num[i],num[j],-num[i]-num[j]])

s = Solution()
l = [-1,0,1]
print s.threeSum(l)