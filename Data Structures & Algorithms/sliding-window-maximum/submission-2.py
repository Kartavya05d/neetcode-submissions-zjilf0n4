class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        res = []

        for i, num in enumerate(nums):
            heapq.heappush(maxHeap, (-num, i))
            if i < k-1: continue #pass till it atleast becomes k length.
            win_start = i-k+1
            while maxHeap[0][1] < win_start:
                heapq.heappop(maxHeap)
            res.append(-maxHeap[0][0])
        return res
            
