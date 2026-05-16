class TimeMap:

    def __init__(self):
        self.dic = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l = self.dic.get(key, [])
        n = len(l)
        res = ''

        start, end = 0, n - 1
        while start <= end:
            mid = (start + end) // 2
            if l[mid][0] <= timestamp:
                res = l[mid][1]
                start = mid + 1
            else:
                end = mid - 1
        return res