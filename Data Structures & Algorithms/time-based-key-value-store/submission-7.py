class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ''
        
        else:
            key_list = self.dic[key]
            n = len(key_list)
            l, r = 0, n - 1

            if timestamp < key_list[l][0]:
                return ''

            while l <= r:
                mid = (l + r) // 2
                # print('l: ', l, 'r: ', r)
                if key_list[mid][0] == timestamp:
                    return key_list[mid][1]
                elif key_list[mid][0] > timestamp:
                    r = mid - 1
                else:
                    l = mid + 1

            return key_list[r][1]


        