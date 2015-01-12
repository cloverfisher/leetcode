class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        num = len(A)
        if num <= 2:
            return num
        tempword = A[0]
        #newA = []
        #newA.append(A[0])
        flag = 0
        i = 1
        while i < len(A): 
            if A[i] == tempword:
                flag+=1
                if flag >= 2:
                    A.pop(i)
                else:
                    i+=1
            else:
                tempword = A[i]
                flag = 0
                i+=1
        return len(A)
        
s = Solution()
print s.removeDuplicates([1,2,2,2])