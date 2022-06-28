class Solution(object):

    def moveZeroes(self, nums):

        i = 0

        count = 0

        while i < len(nums):
            if nums[count] == 0:
                nums.append(nums.pop(count))

            else:
                count += 1

            i += 1
