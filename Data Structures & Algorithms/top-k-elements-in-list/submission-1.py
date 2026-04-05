class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        print(hashmap)
        res = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
        print(res)
        l = list(res.keys())
        return l[:k]