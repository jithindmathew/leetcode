from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        ans = []

        a = Counter(nums1)

        b = Counter(nums2)

        for i in a:
            if i in b:
                ans += [i]*min(a[i], b[i])
        return ans
