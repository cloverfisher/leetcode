class Solution:
	# @param A, a list of integers
	# @return an integer
	
	def trap(self,A):
		stack = []
		stacktopnum = 0
		rainwater = 0

		if len(A) < 3:
			return rainwater
		stack.append(0)
		stacktopnum = 1
		import pdb
#		pdb.set_trace()
		for trapnum in range(1,len(A)):
#			print "trapnum:" , trapnum , " water:" , rainwater , "stack" , stack
			while(stacktopnum >0):
				top = stack.pop()
				stacktopnum = stacktopnum-1
				if stacktopnum == 0:
					if A[top] > A[trapnum]:
						stack.append(top)
						stack.append(trapnum)
						stacktopnum = stacktopnum + 2
						break
					else:
						rainwater = rainwater - (trapnum - top -1) * (A[trapnum] - A[top])
#						print "rainwater" , rainwater , "trapnum" , trapnum , "top" , top
						stack.append(trapnum)
						stacktopnum = stacktopnum + 1
#						print stack
						break
				if A[top] < A[trapnum]:
					tempnum = stack.pop()
					rainwater=rainwater + (top- tempnum)*(A[trapnum]-A[top]) 
#					print "rainwater" , rainwater , "trapnum" , trapnum , "top" , top , "tempnum" , tempnum
					stack.append(tempnum)
				else:
					stack.append(top)
					stack.append(trapnum)
					stacktopnum = stacktopnum + 2
					break
			#	stack.append(trapnum)
		return rainwater

s = Solution()
a = [0,1,0,2,1,0,1,3,2,1,2,1]
a = [4,2,3]
print s.trap(a)
