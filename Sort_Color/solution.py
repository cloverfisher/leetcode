class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        red = 0
        white1 =0
        blue2 = 0
        if(len(A)<=1):
            return A
        for i in A:
            if i == 0:
                red+=1
            elif i == 1:
                white1 +=1
            elif i == 2:
                blue2 +=1
        for i in range(len(A)):
            if(i<red):
                A[i]=0
            elif(i<red+white1):
                A[i]=1
            else:
                A[i]=2
        return A