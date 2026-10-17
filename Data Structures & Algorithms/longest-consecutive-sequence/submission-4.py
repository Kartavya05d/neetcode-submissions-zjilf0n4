class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxCnt, cnt = 0, 0
        sett = set(nums)
        for num in sett:
            if num-1 not in sett:
                cnt = 1
                while num+1 in sett:
                    num+=1
                    cnt+=1
                maxCnt = max(maxCnt, cnt)
        return maxCnt
