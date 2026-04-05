class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = 1, 1
        n = len(nums)
        left_arr = [0]*n
        right_arr = [0]*n

        for i in range(n):
            j = -i-1
            left_arr[i] = left
            right_arr[j] = right
            left *= nums[i]
            right *= nums[j]
        
        return [l*r for l,r in zip(left_arr, right_arr)]