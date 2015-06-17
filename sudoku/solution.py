class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    vertical = {}
    horizontal = {}
    square = {}
    
    def solveSudoku(self, board):

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    continue
                else :
                    self.addNum(i,j,board[i][j])
        
    def addNum(self,i,j,num):
        n = self.horizontal.get(i,[])
        n.append(num)
        self.horizontal[i] = n
        n = self.vertical.get(j,[])
        n.append(num)
        self.vertical[j] = n
        k = i/3*3+j/3
        n = self.square.get(k,[])
        n.append(num)
        self.square[k] = n

    def rmNum(self,i,j,num):
        n = self.horizontal.get(i,[])
        n.remove(num)
        self.horizontal[i] = n
        n = self.vertical.get(j,[])
        n.remove(num)
        self.vertical[j] = n
        k = i/3*3+j/3
        n = self.square.get(k,[])
        n.remove(num)
        self.square[k] = n
 #   def test(self):


s =  Solution()
#s.solveSudoku([])

s.addNum(1,1,3)