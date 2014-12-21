class Solution:
	def numDecodings(self,s):
		alist = []
		alist.append(1)
		if not  s:
			return 0
		elif s[0] == '0':
			return 0
		elif(len(s)==1):
			if s == '0':
				return 0
			else:
				return 1
		elif(len(s)>1):
			if(s[1] == '0' and s[0] <='2'):
				alist.append(1)
			elif(s[1] == '0' and s[0] >'2'):
				return 0
			elif ((s[0] == '2' and s[1]<='6') or (s[0]=='1' )):
				alist.append(2)
			else:
				alist.append(1)
			for i in range (2, len(s)):
				if(s[i-1] == '0' and s[i] == '0'):
					return 0
				elif(s[i-1] > '2' and s[i] == '0'):
					return 0
				elif(s[i] == '0' and s[i-1]!='0'):
					alist.append(alist[i-2])
				elif ((s[i-1] == '2' and s[i]<='6') or (s[i-1]=='1' )):
					alist.append(alist[i-2]+alist[i-1])
				else:
					alist.append(alist[i-1])
			return alist[len(s)-1]
s = Solution()
print s.numDecodings("10")
