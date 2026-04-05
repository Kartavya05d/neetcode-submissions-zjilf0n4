class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            #We are in left sorted array
            if nums[l] <= nums[mid]:
                if nums[l] <= target and nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target >= nums[mid] and target <= nums[r]:
                    l = mid+1
                else:
                    r = mid - 1
        return -1

