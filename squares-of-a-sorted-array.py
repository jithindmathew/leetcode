class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        i = 0
        j = len(nums) - 1

        while i <= j:
            if nums[j]**2 > nums[i]**2:
                nums[j] = nums[j]**2
                j -= 1
            else:
                temp = nums.pop(0)
                nums.insert(j, temp*temp)
                j -= 1
        return nums
