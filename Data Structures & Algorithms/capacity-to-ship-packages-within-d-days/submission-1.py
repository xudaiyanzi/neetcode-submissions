class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_weight, sum_weight = max(weights), sum(weights)

        l, r = max_weight, sum_weight
        res = sum_weight
        n = len(weights)

        while l <= r:
            curr_cap = (l + r) // 2
            curr_days = 1
            w_sum = 0
            # print('l: ', l, '. r: ', r, '.curr_cap: ', curr_cap)
            for i in range(n):
                if w_sum + weights[i] <= curr_cap:
                    # print('continue add: ', w_sum, ' + weights[i]: ', weights[i])
                    w_sum += weights[i]
                else:
                    curr_days += 1
                    w_sum = weights[i]

            if days < curr_days:
                # print('move l: ', l)
                l = curr_cap + 1
            else:
                # print('move r: ', r)
                res = min(res, curr_cap)
                r = curr_cap - 1
                
        
        return res
                