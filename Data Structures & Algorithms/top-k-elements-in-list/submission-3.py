class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        heap = [] #minheap implementation, heap[0] is always the minimum.
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k: heapq.heappop(heap) #smallest freq element is removed.
        return [num for freq, num in heap]
