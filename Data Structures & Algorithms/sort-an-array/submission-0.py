class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr, L, M, R):
            leftArray, rightArray = arr[L: (M + 1)], arr[M + 1 : (R + 1)]
            p, lp, rp = L, 0, 0
            while lp < len(leftArray) and rp < len(rightArray):
                if leftArray[lp] <= rightArray[rp]:
                    arr[p] = leftArray[lp]
                    lp += 1
                else:
                    arr[p] = rightArray[rp]
                    rp += 1
                p += 1
            while lp < len(leftArray):
                arr[p] = leftArray[lp]
                p += 1
                lp += 1
            while rp < len(rightArray):
                arr[p] = rightArray[rp]
                p += 1
                rp += 1

        def divide(arr, l, r):
            if l == r:
                return arr
            mid = (l + r) // 2
            divide(arr, l, mid)
            divide(arr, mid + 1, r)
            merge(arr, l, mid, r)
        
        divide(nums, 0, len(nums) - 1)
        return nums
