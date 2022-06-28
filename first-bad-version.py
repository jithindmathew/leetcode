# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n

        while left < right:
            mid = (left + right) // 2
            print(mid)
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid

        return left
