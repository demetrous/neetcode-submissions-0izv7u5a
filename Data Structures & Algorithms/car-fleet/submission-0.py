class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = [(p, s) for p, s in zip(position, speed)]
        fleets.sort(reverse=True)
        stack = []

        for i in range(len(fleets)):
            time = (target - fleets[i][0]) / fleets[i][1]
            if not stack or (stack and stack[-1] < time):
                stack.append(time)

        return len(stack) 
