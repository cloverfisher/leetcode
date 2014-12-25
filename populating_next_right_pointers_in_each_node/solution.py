class Solution:
#@param root , a tree node 
#@return nothing
	def connect(self,root):
		a = []
		if root != None:
			a.append(root)
			self.queueOperation(a)


	def queueOperation(self,queueA):
		if len(queueA) == 0:
			return None
		queueB = []
		for i in queueA:
			queueB.append(i.left)
			queueB.append(i.right)
		for i in range ((len(queueB)) - 1):
			queueB[i].next = queueB[i+1]
		self.queueOperation(QueueB)
			
