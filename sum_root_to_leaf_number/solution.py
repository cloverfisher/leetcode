# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    totlesum = 0
    def sumNumbers(self, root):
        p = root
        if p == None:
            return 0
        else:
            return self.recursionNum(root,root.val)
    
    def recursionNum(self, root , currentNum):
        p = root
        if p == None:
            return currentNum
        else:
            right = 0
            left = 0
            if p.right != None:
                right = self.recursionNum(p.right,p.right.val + currentNum*10)
            else:
                right = 0
            if p.left != None:
                left = self.recursionNum(p.left,p.left.val + currentNum*10)
            else:
                left =0
            if(p.right==None and p.left == None):
                #this is a leaf
                currentNum = currentNum
            else:
                currentNum = left+right
            return currentNum