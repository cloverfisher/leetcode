# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        nodelist = []
        loop = 0
        newhead = ListNode(None)
        newhead.next = head
        p0 = newhead
        p1 = newhead
        while(True):
            del nodelist[:]
            p0=p1
            for i in range(k):
                p0 = p0.next
                if(p0 == None):
                    return newhead.next
                nodelist.append(p0)
 
            nodelist[0].next = nodelist[k-1].next
            for i in range(1,k):
                nodelist[i].next = nodelist[i-1]
            p1.next = nodelist[k-1]
            p1 = nodelist[0]
        return newhead.next
            
        