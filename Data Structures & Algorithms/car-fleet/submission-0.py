class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for p , s in zip(position, speed):
            cars.append([p,s])

        # Sorts sublists based on value at index 0, in descending order
        cars.sort(key=lambda x: x[0], reverse=True)

        stack = []

        for curr_p, curr_s in cars:
            # case: stack is empty, always push car into stack
            if not stack:
                stack.append([curr_p, curr_s])
            else:
                # case: stack not empty
                # need to compute time at top of stack & curr time
                # IF time_TOP >= time_curr: push current car onto stack
                # OTHERWISE, ignore this car
                time_top = (target - stack[-1][0])/ stack[-1][1]
                time_curr = (target - curr_p) / curr_s

                if time_top < time_curr:
                    stack.append([curr_p, curr_s])
        
        return len(stack)