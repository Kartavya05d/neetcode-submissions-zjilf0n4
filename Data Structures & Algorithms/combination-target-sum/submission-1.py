class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target: #success
                res.append(curr.copy())
                return
            if i >= len(nums) or total > target: #fail
                return
            
            curr.append(nums[i]) #reuse the index
            dfs(i, curr, total+nums[i])
            curr.pop() #move with next element.
            dfs(i+1, curr, total)

        dfs(0, [], 0)
        return res
