class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and stack[-1]>0 and asteroid<0 and abs(stack[-1])<abs(asteroid):
                stack.pop()
            if stack and stack[-1]>0 and asteroid<0 and abs(stack[-1])==abs(asteroid):
                stack.pop()
                continue
            elif stack and stack[-1]>0 and asteroid<0 and abs(stack[-1])>abs(asteroid):
                continue                    
            stack.append(asteroid)
        return stack

