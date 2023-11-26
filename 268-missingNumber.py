class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        ptr1 = 0
        ptr2 = 0
        while ptr1 < len(nums):
            if ptr1 == nums[ptr2]:
                ptr1 += 1
                ptr2 += 1
            else: 
                return ptr1
        return ptr1  