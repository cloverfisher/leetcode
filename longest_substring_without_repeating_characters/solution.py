class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        arr = []
        maxlen = 0
       	for i in s:
            if(i not in arr):
            	arr.append(i)
          #  	print(i,len(arr))
            	if(len(arr)> maxlen):
            		maxlen = len(arr)
            else:
            	arrindex = arr.index(i)
            	k = arr[arrindex+1:len(arr)]
            	arr = k
          #  	print arr
            	arr.append(i)
        return maxlen


a= [1,2,3,1,5,6]
#a = a + a
print(a)
s = Solution()
print s.lengthOfLongestSubstring(a)
