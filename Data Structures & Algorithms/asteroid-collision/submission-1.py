class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []

        for val in asteroids:
            alive = True
            while alive and res and res[-1] > 0 and val < 0:
                if abs(val) > res[-1]:
                    res.pop()
                    alive = True
                elif abs(val) == res[-1]:
                    res.pop()
                    alive = False
                elif abs(val) < res[-1]:
                    alive = False
            if alive:
                res.append(val)
        
        return res
                