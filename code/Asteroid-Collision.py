class Solution(object):

    def asteroidCollision(self, asteroids, prev=[]):
        stack = []
        newAsteroids = list(asteroids)
        while (len(asteroids) > 0):
            while ((len(stack) > 0) and (asteroids[0] < 0) and (stack[(-1)] > 0) and (abs(asteroids[0]) > stack[(-1)])):
                stack.pop((-1))
            x = asteroids.pop(0)
            if (x > 0):
                stack.append(x)
            elif (len(stack) == 0):
                stack.append(x)
            elif (abs(x) == stack[(-1)]):
                stack.pop((-1))
            elif (abs(x) > stack[(-1)]):
                stack.append(x)
            elif (stack[(-1)] < 0):
                stack.append(x)
        return stack
        if (stack == prev):
            return stack
        else:
            return self.asteroidCollision(newAsteroids, stack)