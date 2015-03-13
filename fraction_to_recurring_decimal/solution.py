class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        decimal = numerator%denominator
        integer = (numerator-decimal)/denominator
        index = {}
        indexarr = []
        decimalOutputCache = []
        r = str(integer)
        r1 = ""  # r1 is decimal part
        if(decimal>0):
        	z = decimal
        	index[decimal] = 1
        	indexarr.append(decimal)
#         	decimalOutputCache.append(k)
        	while(decimal!=0):
        		decimal = decimal*10
        		z = decimal%denominator
        		k = (decimal-z)/denominator
        		decimal = z
        #		print "22" , k, "k",decimal,"decimal"
        #		print index 
        		if(decimal==0):  #not a loop decimal
        			decimalOutputCache.append(k)
        			r = r + '.'
        			for i in decimalOutputCache:
        				r = r + str(i)
        			break
    #    		r = r + str(k)
        		if(index.has_key(decimal)):#loop end
        			r = r + '.'
        			index = indexarr.index(decimal)
        			decimalOutputCache.append(k)
        	#		print "index " , index , "decimal" , decimal
        			for i in range(0,index):
        				r = r + str(decimalOutputCache[i])
        			r = r + '('
        	#		print len(decimalOutputCache)
        	#		print "decimalOutCache" ,decimalOutputCache
        	#		print "indexarr",indexarr
        			for i in range(index,len(decimalOutputCache)):
        				r = r + str(decimalOutputCache[i])
        			r = r + ')'
        			break
         		else:
         			index[decimal] = 1
        			indexarr.append(decimal)
        #			print k, "k",decimal,"decimal"
        			decimalOutputCache.append(k)
		# 			index[decimal] = 1
		# 			indexarr.append(decimal)
		# #			decimalOutputCache.append(k)
		# 			print "a"
        return r

s = Solution()
print s.fractionToDecimal(2,1)