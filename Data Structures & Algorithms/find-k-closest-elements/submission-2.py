class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # find the index closet to x
        n = len(arr)
        l, r = 0, n - 1
        while l < r:
            mid = (r + l) // 2
            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid
        
        ## expand the window
        go_l, go_r = l - 1, l

        while go_r - go_l - 1 < k:
            if go_l < 0:
                go_r += 1
            elif go_r > n - 1:
                go_l -= 1
            elif abs(arr[go_r] - x) >= abs(arr[go_l] - x):
                go_l -= 1
            else:
                go_r += 1
        
        return arr[go_l + 1: go_r]