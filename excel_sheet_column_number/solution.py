class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        l = len(s)
        num =0
        for i in s:
            num=num*26+ord(i)-ord('A')+1  	#ord  is "char convert to ascII" chr is "ascII convert to char" 
        return num