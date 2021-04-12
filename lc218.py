# Apr/11/2021
# LC 218 --- The Skyline Problem
# 参考一姐方法，Python heap不支持remove所以手写一个heap

from heapq import *
class Heap(object):
    def __init__(self):
        self.heap1 = []
        self.heap2 = []
    def push(self, num):
        heappush(self.heap1, num)
    
    def remove(self, num):
        if num == self.heap1[0]:
            heappop(self.heap1)
            return
        heappush(self.heap2, num)
    
    def top(self):
        while self.heap2 and self.heap1[0] == self.heap2[0]:
            heappop(self.heap1)
            heappop(self.heap2)
        return self.heap1[0]
    def pop(self):
        while self.heap2 and self.heap1[0] == self.heap2[0]:
            heappop(self.heap1)
            heappop(self.heap2)
        return heappop(self.heap1)
    def size(self):
        return len(self.heap1) - len(self.heap2)
class Solution(object):
    def getSkyline(self, buildings):、
        res = []
        skylines = []
        for left, right, height in buildings:
            skylines.append([left, -height])
            skylines.append([right, height])
        skylines.sort(key=lambda x: (x[0], x[1]))
        maxHeap = Heap()
        maxHeap.push(0)
        max_height = 0
        ans = []
        for x, y in skylines:
            if y < 0:
                maxHeap.push(y)
            else:
                maxHeap.remove(-y)
            if max_height != maxHeap.top() * (-1):
                max_height = -maxHeap.top()
                ans.append([x, max_height])
        return ans
