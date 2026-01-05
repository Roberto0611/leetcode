def asteroidCollision(asteroids):
        stack = []

        for asteroid in asteroids:
            if not stack or asteroid > 0:
                stack.append(asteroid)
                continue

            # si el asteroide es negativo
            while True:
                if len(stack) == 0 or stack[-1] < 0:
                    stack.append(asteroid)
                    break

                if abs(asteroid) > stack[-1]:
                    stack.pop()
                    continue

                if abs(asteroid) == stack[-1]:
                    stack.pop()
                    break
    
                break

        return stack

# testcase
asteroids = []
print(asteroidCollision(asteroids))