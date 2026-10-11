class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right, n = 1, 1, len(nums)
        l_arr = [0]*n
        r_arr = [0]*n
        for i in range(n):
            j = -i-1
            l_arr[i] = left
            r_arr[j] = right
            left *= nums[i]
            right *= nums[j]
        return [l*r for l, r in zip(l_arr, r_arr)]
