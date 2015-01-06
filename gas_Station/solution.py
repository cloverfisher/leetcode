class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        sum = 0
        length = len(gas)
        for i in range(length):
            sum = sum + gas[i] - cost[i]
        if sum < 0 :
            return -1
        profit = []
        for i in range(length):
            profit.append(gas[i] - cost[i])
        for i in range(length):
            profit.append(gas[i]-cost[i])
        flag = 0
        tag = 0
        sum = 0
        for flag in range(0,length):
            sum = sum + profit[flag]
            if(sum < 0):
                sum = 0
                tag = flag+1
        return tag