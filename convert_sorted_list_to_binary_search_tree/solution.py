# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        right = None
        left = None
        root = None
        if(head == None):
            return None
        if(head.val == None):
            return None
        a = self.findMid(head)
        if(a == None):
            root = TreeNode(None)
            return root
        else:
            root = TreeNode(a.val)
        if(a.next!=None):
            right = self.sortedListToBST(a.next)
        a.val = None
        a= None
        left = self.sortedListToBST(head)
        root.left = left
        root.right = right
        return root
        #left = 3
        
        
    def findMid(self, head):
        p1 = head
        p2 = head
        if(head == None or head.val == None):
            return head
        while(True):
            if(p2.next == None):
                break
            if(p2.next.val == None):
                break
            p1 = p1.next
            p2 = p2.next.next
            if(p2 == None):
                break
            if(p2.val ==None):
                break
        return p1