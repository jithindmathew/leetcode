class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        cnt = 0
        for i, ch in enumerate(s1):
            if ch not in s2:
                return False
            else:
                if s1[i] != s2[i]:
                    cnt += 1
        return cnt == 2 or cnt == 0
