class Solution:
	def solveNQueens(self,n):

		result = []
		arrx = []
		dicx = {}
		self.lovequeen(0,arrx,n,dicx,result)
		return result

	def lovequeen(self,y,arrx,n,dicx,result):
		if(y == n):
			#every row has a Queena
			onesolution = []
			for i in range(n):
				rowstr = ''
				for j in range(n):
					if arrx[i] ==j :
						rowstr+='Q'
					else:
						rowstr+='.'
	#			print rowstr
				onesolution.append(rowstr)

	#		print "onesolution", onesolution
			result.append(onesolution)
			return result
		for i in range(n):
			# y = y, x = i
			if dicx.get(i,0) == 0:
				# x is ok then consiider the sider way.
				occupy  = False
				for j in range (y):
					if abs(y-j) == abs(i - arrx[j]):
						occupy = True
				if occupy == False:
					#x y can be a Queen:
					arrx.append(i)
					dicx[i] = 1
					self.lovequeen(y+1,arrx,n,dicx,result)
					dicx[i] = 0
					arrx.remove(i)
		return result


s = Solution()
print "solution" , s.solveNQueens(4)
