class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = []
        for row in matrix:
            res.extend(row)
        
        l, r = 0, len(res)-1

        while l <= r:
            mid = (l+r)//2
            if res[mid] == target:
                return True
            elif res[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False