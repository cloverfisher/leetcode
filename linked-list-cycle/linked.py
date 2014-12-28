# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        point1 = head
        point2 = head
        i = 0
        while(i<100000):
            if point1 == None:
                return False
            if point1.next == None:
                return False
            if point1.next.next == None:
                return False
            point1 = point1.next.next
            point2 = point2.next
            if(point1 == point2):
                return True
            else:
                i = i+1
        return False