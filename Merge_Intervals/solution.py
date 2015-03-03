# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        length  = 10000
        arr = []
        resultlist = []
        state = 0 # state = 0, when arr[i] = 0, state <- 1, and begin merge
        start = 0
        end = 0
        if(len(intervals)<=1):
            return intervals
        for i in range(0,length):
            arr.append(1)

        for interval in intervals:
            if(interval.start==interval.end):
                arr[interval.start*2]=0
            else:
                for i in range(interval.start*2,interval.end*2):
                    arr[i]=0
        for i in range(length):
            if (state==0):
                if (arr[i] ==0):
                    state = 1
                    start = i/2
            elif(state==1):
                if(arr[i]==1):
                    state = 0
                    end = i/2
                    newinterval=Interval(start,end)
                    resultlist.append(newinterval)
        return resultlist