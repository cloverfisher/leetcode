class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if(numRows < 2):
            return s
        str1 = []
        for i in range (numRows):
            str1.append("")
        print len(str1)
        l = numRows*2 - 2
        for i in range(0,len(s)):
            t = i % l
            if(t<numRows-1):  #zig
                str1[t]+=s[i]
            else:
                print(2*numRows- t-2 )
                str1[2*numRows- t-2]+=s[i]
        result = ""
        for i in str1:
            result += i
        return result
                
            
s = Solution()
string = "A"
n = 1
print s.convert(string,n)
