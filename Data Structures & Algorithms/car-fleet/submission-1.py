class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = [(p, s) for p, s in zip(position, speed)]
        fleets.sort(reverse=True)
        stack = []

        for p, s in fleets:
            time = (target - p) / s
            if not stack or (stack and stack[-1] < time):
                stack.append(time)

        return len(stack) 