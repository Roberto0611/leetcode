def carFleet(target,position, speed):
        pair = [(p, s) for p, s in zip(position, speed)]
        stack = []
        pair.sort(reverse=True)

        for p,s in pair:
            if len(stack) == 0 or (target - p)/s > stack[-1]:
                stack.append((target - p)/s)
            
        return len(stack)

# testcase
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
print(carFleet(target,position,speed))