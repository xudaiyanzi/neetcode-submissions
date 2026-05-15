class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_pairs = sorted(zip(position, speed), reverse=True)
        fleet = 0
        slowest_time_ahead = 0

        for pos, spd in car_pairs:
            time = (target - pos) / spd

            if time > slowest_time_ahead:
                fleet += 1
                slowest_time_ahead = time
        
        return fleet