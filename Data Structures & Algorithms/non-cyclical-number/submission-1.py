class Solution:
    def isHappy(self, n: int) -> bool:
        sett = set()

        while n != 1:
            if n in sett:
                return False

            sett.add(n)

            nextsum = 0
            while n:
                nextsum += (n % 10) ** 2
                n //= 10

            n = nextsum

        return True