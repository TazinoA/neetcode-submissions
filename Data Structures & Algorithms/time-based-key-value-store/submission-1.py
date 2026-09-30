class TimeMap:

    def __init__(self):
        self.hashMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap:
            self.hashMap[key] = [[value, timestamp]]
        else:
            self.hashMap[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashMap:
            return ""
        
        for value,prevTime in self.hashMap[key][::-1]:
            if prevTime <= timestamp:
                return value
        
        return ""
