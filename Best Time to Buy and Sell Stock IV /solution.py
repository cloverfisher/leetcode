class Solution:
    # @return an integer as the maximum profit 
    def maxProfit(self, k, prices):
        l = len(prices)
        alist = []
        for i in range(0,l):
        	alist.append(i)

        for i in range(0,l):
        	for j in range(i+1,l):
        		if(prices[j] < prices[i]):
        			tmp = prices[j]
        			prices[j] = prices[i]
        			prices[i] = tmp
        			tmp = alist[j]
        			alist[j] = alist[i]
        			alist[i] = tmp
        # after this prices will be a sorted prices and alist will be the origin place number of prices
        print alist
        print prices

        while(k>=2):
        	k-=2
        	l1 = len(prices)
        	if(l1<2):
        		break
        	purchasePlace = 0
        	sellPlace = l1-1
        	purchasePrice = prices[0]
        	sellPrice = prices[l1-1]
        	if(alist[])



s = Solution()
s.maxProfit(2,[3,1,5,6,4,9])