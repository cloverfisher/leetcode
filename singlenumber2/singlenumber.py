class Solution:
	def singleNumber(self, A):
		d = {}
		for i in A:
	#		print i
			d[i] = d.get(i,0)+1
			if(d[i]==3):
				d.pop(i)
	#	d['3'] = 5
		return d.keys()[0]

        
s = Solution()
print s.singleNumber([5,5,5,3,2,3,3])