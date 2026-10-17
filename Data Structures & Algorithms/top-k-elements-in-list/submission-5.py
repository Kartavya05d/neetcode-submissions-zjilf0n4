class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
        heap = []
        for key in count.keys():
            heapq.heappush(heap, (count[key], key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for freq, num in heap]
