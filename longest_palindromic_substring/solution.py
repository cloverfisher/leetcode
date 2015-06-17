class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        l = len(s)
        max = 1
        maxindex = 0
        if(l<=1):
            return s
        # if(l == 2):
        #     return s[0]
        i=0
        maxindex = 0
        while (i+1<l):
            p = 1
            if(s[i] == s[i+1]):
                p+=1

                if(p>max):
                    max = p
                    maxindex = i
                k = i+1
                while(k+1<l):
                    k+=1
                    if(s[k]!=s[i]):
                        k = k-1
                        break
                    else:
                        p+=1
                        if(p>max):
                            max = p
                            maxindex = i
                o = 1
                while(k+o<l and i-o>=0):
                    if(s[k+o] == s[i-o]):
                        p+=2
                        if(p>max):
                            max = p
                            maxindex = i - o
                        o+=1
                    else:
                        break
                i = k+1
            elif(i+1<l and i -1 >=0):
                if(s[i+1]!=s[i-1]):
                    i = i+1
                    continue
                else:
                    p+=2
                    if(p>max):
                        max = p
                        maxindex = i -1
                    k = 2
                    while(i+k<l and i-k>=0):
                        if(s[i+k]!=s[i-k]):
                            break
                        else:
                            p+=2
                            if(p>max):
                                max = p
                                maxindex = i - k
                            k+=1
                i+=1
            else:
                i+=1
    #            print(60,i)
        return s[maxindex:maxindex+max]
                


s = Solution()
a = "lqlvciwekzxapmjxyddlaoqhfhwphamsyfwjinkfvciucjhdgwodvmnpkibumexvlsxxumvrznuuyqfavmgwfnsvfbrvqhlvhpxaqehsiwxzlvvtxsnmlilbnmvnxyxitxwoahjricdjdncvartepfpdfndxqoozkfpdmlpvshzzffsspdjzlhmamqooooor"
print s.longestPalindrome(a)