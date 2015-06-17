class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        tag = 1
        maxint = 2147483647
        if(divisor == 0):
            return maxint
        if(dividend == 0):
            return 0
        if(divisor == 1):
            return dividend
        if((dividend > 0 and divisor< 0)or(dividend < 0 and divisor > 0)):
            tag = 0
        if(dividend<0):
            dividend = -dividend
        if(divisor<0):
            divisor = - divisor
        origin = dividend
        result = 0
        while True:
            temp = divisor
            temp1 = 1
            
            if(dividend < divisor):
                return self.negative(tag,result)
            while(dividend > 0):
                dividend-= temp
                if(dividend<0):
                    break
                temp+=temp #1,3,7
                result += temp1
                temp1+=temp1 #1,2,4,8
            if(dividend==0):
                return self.negative(tag,result)
            dividend+=temp
            if(dividend>origin):
                return self.negative(tag,result)
            origin = dividend

    def negative(self,tag,number):
        if(number>2147483647):
            return 2147483647
        if(tag==0):
            return 0-number
        return number

s = Solution()
print s.divide(-1,1)