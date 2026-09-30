class TimeMap:

    def __init__(self):
        self.hashMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap:
            self.hashMap[key] = []
        self.hashMap[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashMap:
            return ""
        
        l, r = 0, len(self.hashMap[key]) - 1
        res = ""
        while l <= r:
            mid = (l+r)//2
            value, prevTime = self.hashMap[key][mid]
            if prevTime <= timestamp:
                res = value
                l = mid+1
            else:
                r = mid - 1
        
        return res
