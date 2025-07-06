class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(positionOfCar,speedOfCar) for positionOfCar,speedOfCar in zip(position,speed)]
        cars.sort(key=lambda x:x[0])
        stack = []
        n = len(cars)
        for i in range(n-1,-1,-1):
            timeToReach = (target-cars[i][0])/cars[i][1]
            if len(stack)>0 and timeToReach>stack[-1]:
                stack.append(timeToReach)
            else:
                if len(stack)==0: stack.append(timeToReach)
        
        return len(stack)
        