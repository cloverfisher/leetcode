class Solution:
	def combine(self,n,k):
		alist = []
		alist2 = []
		alist3 = []
		if(n==k):
			return [[x for x in range(1,n+1)]];
		elif(k==0):
			return [[]]
		else:
			for i in range(k,n+1):
				alist2 = self.combine(i-1,k-1)
				if(len(alist2)>0): 
					for alist3 in alist2:
						alist3.append(i)
						alist.append(alist3)
				else:
					alist2.append(i)
					alist.append(alist2)
			return alist
	def __init__(self,n,k):
	 	print self.combine(n,k)


a = Solution()
print a.combine(6,4)
