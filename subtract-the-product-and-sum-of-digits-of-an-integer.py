class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        pro = 1
        for i in str(n):
            sum = sum + int(i)
            pro = pro*int(i)
        return pro-sum
