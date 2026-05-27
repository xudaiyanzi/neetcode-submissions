from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        frequency = max(count.values())

        max_count = 0

        for k, v in count.items():
            if v == frequency:
                max_count += 1
        
        res = (frequency - 1) * (n + 1) + max_count

        return max(res, len(tasks))