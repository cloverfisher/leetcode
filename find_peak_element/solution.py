class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        l = len(num)
        r = []
        if (l<=1):
            return 0
        elif (l==2):
            if(num[0]>num[1]):
                return 0
            else:
                return 1
        else:
            for i in range(1,l-1):
                if(num[i]>num[i-1] and num[i]>num[i+1]):
                    return i
            if(num[0]>num[1]):
                return 0
            if(num[l-1]>num[l-2]):
                return l-1
        return 0