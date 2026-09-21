class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position,speed)]
        pair.sort(reverse=True) #Nearest -> Farthest
        stack = []
        for p, s in pair:
            time = (target-p)/s
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]: #new car reaches earlier?
                stack.pop() #if new car is faster, pop it, because it will run as per slow car
        return len(stack)            
