class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        ans = float('inf')
        while left <= right:
            mid = (left + right) // 2
            #Only first time
            if (nums[left] <= nums[right]):
                return min(ans, nums[left])
            elif (nums[left] <= nums[mid]): #Left side sorted
                ans = min(ans, nums[left])
                left = mid+1
            else: #Right is sorted
                ans = min(ans, nums[mid])
                right = mid-1
        return ans
