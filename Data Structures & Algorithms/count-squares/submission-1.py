class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        x, y = point[0], point[1]
        if (x, y) in self.points:
            self.points[(x, y)] += 1
        else:
            self.points[(x, y)] = 1
        

    def count(self, point: List[int]) -> int:
        x, y = point[0], point[1]
        res = 0

        for (nx, ny), c in self.points.items():
            if nx != x or ny == y:
                continue
            
            size = y - ny

            count1 = self.points.get((x + size, y), 0)
            count2 = self.points.get((x + size, ny), 0)
            count3 = self.points.get((x, ny), 0)
            ans1 = count1 * count2 * count3

            count4 = self.points.get((x - size, y), 0)
            count5 = self.points.get((x - size, ny), 0)
            ans2 = count4 * count5 * count3 

            res += ans1 + ans2
        
        return res
        
        
