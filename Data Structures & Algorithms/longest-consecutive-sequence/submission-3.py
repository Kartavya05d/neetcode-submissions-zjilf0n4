class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cnt = 0
        maxCnt = 0
        sett = set(nums)
        for num in sett:
            if num-1 not in sett: #this is start of sequence.
                cnt = 1
                while num+1 in sett:
                    num+=1
                    cnt+=1
                maxCnt = max(maxCnt, cnt)
        return maxCnt
