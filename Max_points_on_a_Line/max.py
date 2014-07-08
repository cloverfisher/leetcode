#Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
    def __getitem__(self,item):
        return (self.x,self.y)[item]
    

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
		Dx={}
		Dy={}
		Dmin={}
		Dadd={}
		ma = 0
		for i in points:
			p = Point(i[0],i[1])
			if(Dx.has_key(p.x)):
				Dx.update({p.x:Dx[p.x]+1})
			else:
				Dx.update({p.x:1})
			if(Dy.has_key(p.y)):
				Dy.update({p.y:Dy[p.y]+1})
			else:
				Dy.update({p.y:1})
			if(Dmin.has_key(p.y-p.x)):
			    Dmin.update({p.y-p.x:Dmin[p.y-p.x]+1})
			else:
			    Dmin.update({p.y-p.x:1})
			if(Dadd.has_key(p.y+p.x)):
			    Dadd.update({p.y+p.x:Dadd[p.y+p.x]+1})
			else:
			    Dadd.update({p.y+p.x:1})
		values = Dx.values() + Dy.values() + Dmin.values() + Dadd.values()
		returnvalue = 0
		for i in values:
			if (returnvalue < i):
				returnvalue = i
		return returnvalue   
        

so = Solution()
print so.maxPoints([(1,1),(1,2)])