class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize: return False

        count = Counter(hand) #makes freq table
        hand.sort()

        for num in hand:
            if count[num]:
                for i in range(num, num+groupSize):
                    if not count[i]: return False #next higher number.
                    count[i] -= 1
        return True
