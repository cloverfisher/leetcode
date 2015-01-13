# the leetcode is boring but this automata is interesting 
class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        if s == None:
            return False
        s=s.strip()
        if len(s) == 0:
            return False
        if s.isdigit():
            return True
        
        state = [0,1,2,3,4,5,6,7]
        #signal :   num ->0,
        #           "+-" ->1, 
        #           "."->2,
        #           "e"   ->3
        #           else  -->4
        #       0           1                 2[1,-1,3,5]   3               4               5             6               7
        table = [[1,2,3,-1,-1],[1,-1,4,5,-1],[1,-1,3,-1,-1],[4,-1,-1,-1,-1],[4,-1,-1,5,-1],[6,7,-1,-1,-1],[6,-1,-1,-1,-1],[6,-1,-1,-1,-1]]
        #1,4,6 is out state
        currentState = 0
        signal = 4
        for i in s:
            if i <= '9' and i >= '0':
                currentState = table[currentState][0]
            elif i == '+' or i == '-':
                currentState = table[currentState][1]
            elif i == '.':
                currentState = table[currentState][2]
            elif i == 'e' or i == 'E':
                currentState = table[currentState][3]
            else:
                return False
            if currentState == -1:
                return False
        if currentState == 1 or currentState == 4 or currentState == 6:
            return True
        else:
            return False
            
        