class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        dic = {"2":['a','b','c'],"3":['d','e','f'],\
        "4":['g','h','i'],"5":['j','k','l'],"6":['m','n','o'],\
        "7":['p','q','r','s'],"8":['t','u','v'],"9":['w','x','y','z']}
        l = len(digits)
        if(l<1):
            return []
        if(l == 1):
            if digits[0] in dic:
                return dic[digits[0]]
            else:
                return []
        else:
            if(digits[l-1] not in dic):
                return []
            k = dic[digits[l-1]]
            a = self.letterCombinations(digits[:l-1])
            print a
            print k
            result = []
            for i in a:
                for j in k:
                    result.append(i+j)
            return result

s = Solution()
print s.letterCombinations("22")