class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while(j < k):
                current_sum = nums[i] + nums[j] + nums[k]
                if current_sum < 0:
                    j+=1
                elif current_sum > 0:
                    k-=1
                else:
                    current_list = [nums[i], nums[j], nums[k]]
                    res.append(current_list)
                    j+=1
                    k-=1
                    while(j < k and nums[j-1] == nums[j]):
                        j+=1
                    while(j < k and nums[k+1] == nums[k]):
                        k-=1
        return res