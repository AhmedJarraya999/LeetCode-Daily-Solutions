class MedianFinder:

    def __init__(self):
        self.nums=[]

        

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        

    def findMedian(self) -> float:
        self.nums.sort()
        n=len(self.nums)
        mid=n//2
        if n%2==1:
            return self.nums[mid]
        else:
            return (self.nums[mid-1]+self.nums[mid])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()