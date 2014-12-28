class Solution:
	# @param s, a string
	# @param dict, a set of string
	# @return a list of strings
	def wordBreak(self, s, dict):
		solution = []
		a = "".join(set(s))
		b = "".join(set(dict))
		for i in range(len(a)):
			if(b.find(a[i]) == -1):
				return solution 
		self.findWord(s,dict,solution,"")
		return solution

	def findWord(self,s,dict,solution,nowstring):
	#	import pdb
	#	pdb.set_trace()
		for word in dict:
			if(s.find(word) == 0):
				astring = nowstring + " " + word
#				astring = nowstring.join(word+" ")
				if(len(word) == len(s)):
					astring = astring.strip()
					solution.append(astring)
				else:
					substring = s[len(word):]
					self.findWord(substring,dict,solution,astring)

s = Solution()
# string = "bb"
# d = ["a","b","bbb","bbbb"] 
# string = "catsanddog"
# d = ["cat","cats","and","sand","dog"] 
string = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
d =  ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print s.wordBreak(string,d)
		

