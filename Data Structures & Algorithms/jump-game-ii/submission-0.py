class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        farthest_reached_yet = 0
        current_jump_end = 0

        for i in range(len(nums)-1): #We don't want to jump from last place, so no need to include it.
            farthest_reached_yet = max(farthest_reached_yet, i + nums[i])
            if i == current_jump_end:
                jumps+=1
                current_jump_end = farthest_reached_yet
        return jumps
