class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
		length = 0
		aline = [[]]
		linenum = 0
		result = []
		for word0 in words:
			length +=  len(word0)
			if(length > L):
				#change another line
				linenum+=1
				aline.append([word0])
				length = len(word0)
				length +=1
			else:
				aline[linenum].append(word0)
				length +=1
#				print length
		for line in aline:
			length = len(line)
			if length == 1:
				result.append(line[0].ljust(L))
				continue
			wordlength = 0	
			for word in line:
				wordlength+=len(word)
			spacelength = L - wordlength
			newword = ""
			if spacelength == 0:
				#just combine the word
				newword = "".join(line)
				print newword
			else:
				offset = spacelength % (length-1)
				everspace = spacelength / (length-1)
		#		print offset,spacelength,length,everspace				
				for i in range(0,length-1):
					if offset > 0:
						newword = newword + line[i] + " " * (everspace+1)
						offset -= 1
					else:
						newword = newword + line[i] + " " * (everspace)
				newword = newword + line[len(line)-1]
		#		print newword
		#	newword = newword.ljust(L)
			result.append(newword)
		lastline = result[len(result)-1]
		lastline=self.makesameLength(lastline,L)
		result[len(result)-1] = lastline
		return result
    def makesameLength(self, word, L):
		word = word.split()
		word = " ".join(word)
		word = word.ljust(L)
		return word

s = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
L = 14
print s.fullJustify(words,L)
