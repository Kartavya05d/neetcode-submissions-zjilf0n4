class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_multiplier = 1
        right_multiplier = 1
        n = len(nums)
        l_arr = [0]*n
        r_arr = [0]*n

        for i in range(n):
            j = -i-1
            l_arr[i] = left_multiplier
            r_arr[j] = right_multiplier
            left_multiplier *= nums[i]
            right_multiplier *= nums[j]
        return [l*r for l,r in zip(l_arr, r_arr)]