class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(numbers):
            toAdd = target-num
            if toAdd in hashmap:
                return [hashmap[toAdd]+1, i+1]
            hashmap[num] = i
        return [-1,-1]