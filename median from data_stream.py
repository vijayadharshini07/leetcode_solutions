import heapq
class MedianFinder:
    def __init__(self):
        self.small=[]
        self.large=[]
    def addnum(self,num):
        heapq.heappush(self.small,-num)
        if self.small and self.large and (-self.small[0]>self.large[0]):
            heapq.heappush(self.small,-heapq.heappop(self.small))
        if len(self.small)>len(self.large)+1:
            heapq.heappush(self.large,-heapq.heappop(self.small))
        if len(self.large)>len(self.small):
            heapq.heappush(self.small,-heapq.heappop(self.large))
    def findmedian(self):
        if len(self.small)>len(self.large):
            return float(-self.small[0])
        return(-self.small[0]+self.large[0])/2
mf=MedianFinder()
mf.addnum(1)
mf.addnum(2)
print("Median:",mf.findmedian())
mf.addnum(3)
print("Median:",mf.findmedian())
            
            
            
