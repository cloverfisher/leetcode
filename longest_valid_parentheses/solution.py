class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        result = 0
        p=0
        l = len(s)
        flag = 0
        count = []
        stack = []
        state =0
        while(p<l):
            k = s[p]
            p += 1
            if(state == 0):
                print "state0"
                if(k==')'):
                    continue
                elif(k=='('):
                    state =1
                    stack.append(1)
                    count.append(0)
            elif(state == 1):
                print "state1"
                if(k==')'):
                    state = 2
                    stack.pop()
                    currentCount = count.pop()
                    currentCount+=1
                    if(len(count)>0):
                        currentCount2 = count.pop()
                        currentCount += currentCount2

                    #print currentCount
                    count.append(currentCount)
                    # if(count>result):
                    #     result = count
                elif(k=='('):
                    state =3
                    leftParentheses = stack.pop()
                    leftParentheses +=1
                    stack.append(leftParentheses)
                #    count.append(0)
            elif(state == 2):
                print "state2"
                if(k==')'):
                    state = 0

                    currentcount = count.pop()
                    if(currentcount>result):
                        result = currentcount
                    del stack[:]
                    del count[:]
                elif(k == '('):
                    state =1
                    stack.append(1)
                    count.append(0)
            elif(state == 3):
                print "state3"
                if(k==')'):
                    leftParentheses = stack.pop()
                    leftParentheses -=1
                    currentcount = count.pop()
                    currentcount +=1
                    if(leftParentheses==0):
                        if(len(count)>0):
                            currentcount2 = count.pop()
                            currentcount += currentcount2
                    else:
                        stack.append(leftParentheses)                    
                    count.append(currentcount)
                    state = 4
                elif(k=='('):
                    leftParentheses = stack.pop()
                    leftParentheses +=1
                    stack.append(leftParentheses)
            elif(state == 4):
                print "state4"
                print count,stack
                if(k==')'):
                    leftParentheses = stack.pop()
                    leftParentheses -=1
                    currentcount = count.pop()
                    currentcount +=1
                    if(leftParentheses == 0):
                        if(len(count)>0):
                            currentcount2 = count.pop()
                            currentcount2+=currentcount
                            count.append(currentcount2)
                        else:
                            count.append(currentcount)
                        if(len(stack) ==0):
                            state = 2
                    else:
                        stack.append(leftParentheses)
                        count.append(currentcount)
                        state = 4
                elif(k=='('):
                    count.append(0)
                    stack.append(1)
                    state = 3
        if(len(count) > 0):
            currentcount = max(count) 
            if(currentcount > result):
                result = currentcount
        return result*2
                    
                
s = Solution()
pa = "((()))())"
pa = "(()(((()"
pa = "()(())"
print s.longestValidParentheses(pa)