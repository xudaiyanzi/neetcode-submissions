class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        alive = True
        res = []

        for val in asteroids:
            alive = True
            while alive and res and res[-1] > 0 and val < 0:
                if abs(val) > res[-1]:
                    alive = True
                    res.pop()
                elif abs(val) == res[-1]:
                    res.pop()
                    alive = False
                else:
                    alive = False
            if alive:
                res.append(val)
        
        return res

