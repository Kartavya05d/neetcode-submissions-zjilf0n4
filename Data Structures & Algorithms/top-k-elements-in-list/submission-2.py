class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
        reverse_sorted = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
        return list(reverse_sorted.keys())[:k]