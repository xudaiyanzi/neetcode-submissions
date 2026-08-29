class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1

        while l < r:
            mid = (l + r) // 2
            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid
        
        go_l, go_r = l - 1, l

        while go_r - go_l - 1 < k:
            if go_l < 0:
                go_r += 1
            elif go_r > len(arr) - 1:
                go_l -= 1
            elif abs(arr[go_l] - x) <= abs(arr[go_r] - x):
                go_l -= 1
            else:
                go_r += 1
        
        return arr[go_l + 1: go_r]