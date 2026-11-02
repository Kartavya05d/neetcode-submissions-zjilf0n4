class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []

        l1, r1 = 0, 0

        while l1 < len(nums1) and r1 < len(nums2):
            if nums1[l1] < nums2[r1]:
                res.append(nums1[l1])
                l1+=1
            else:
                res.append(nums2[r1])
                r1+=1
        while l1 < len(nums1):
            res.append(nums1[l1])
            l1+=1
        while r1 < len(nums2):
            res.append(nums2[r1])
            r1+=1
        l, r = 0, len(res)
        if len(res) % 2 == 0:
            mid = l + (r-l)//2
            other = mid-1
            print(l)
            print(r)
            print(mid)
            print(other)
            return (res[mid]+res[other]) / 2
        else:
            mid = l + (r-l)//2
            return res[mid]