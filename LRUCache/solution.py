class LRUCache:
    
    lrudic = {}
    lrulength = 0
    capacity = 0
    lrulist = []
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.lrudic.clear()
        self.lrulength = 0
        a = []
        self.lrulist = a 
      #  self.lrulist = []

    # @return an integer
    def get(self, key):
        if self.lrudic.has_key(key):
            self.lrulist.remove(key)
            self.lrulist.append(key)
  #          for i in range(self.lrulength-1, -1 , -1):
   #             if(self.lrulist[i] == key):
    #                del self.lrulist[i]
     #               self.lrulist.append(key)
      #              break
            return self.lrudic[key]
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if self.lrudic.has_key(key): # has key
            self.lrudic[key] = value
            self.lrulist.remove(key)
            self.lrulist.append(key)
 #           for i in range(self.lrulength-1,-1,-1):
 #               if(self.lrulist[i] == key):
 #                   del self.lrulist[i]
 #                   self.lrulist.append(key)
 #                   break
        else:
            self.lrudic[key] = value
            self.lrulist.append(key)
            if self.lrulength == self.capacity:
                del self.lrudic[self.lrulist[0]]
                del self.lrulist[0]
            else: 
                self.lrulength+=1
        