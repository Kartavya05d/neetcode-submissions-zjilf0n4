class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        if x < 0:
            is_negative=True
            x*=-1

        MAX = (2 ** 31) - 1

        res = 0
        while x:
            digit = x % 10
            x = x//10

            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0

            res = (res * 10) + digit

        return -res if is_negative else res
