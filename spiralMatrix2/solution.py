class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        alist = [[-1]*n for i in range(n)]
        
        left = -1
        right = n
        up = -1
        down = n
        x,y = 0,0
        
        h,v = 1,0
        t = 1
    #    alist[0][0] = 1
        for i in range(0,n*n):
            alist[y][x] = i+1
            x+=h
            y+=v
            if(x==right):
                x-=1
                h,v = 0,1
                up+=1
                x+=h
                y+=v
            elif(y == down):
                right-=1
                y-=1
                h,v = -1,0
                x+=h
                y+=v
            elif(x == left):
                down-=1
                x+=1
                h,v = 0,-1
                x+=h
                y+=v
            elif(y == up):
                left+=1
                y+=1
                h,v=1,0
                x+=h
                y+=v
                

            
        return alist
            
                
                
n = 4
s = Solution()
print s.generateMatrix(n)